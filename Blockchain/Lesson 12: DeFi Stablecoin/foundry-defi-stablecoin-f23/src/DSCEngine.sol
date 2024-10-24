// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

/*
 * @title DSCEngine
 * @author Ervand Agadzhanyan
 *
 * The system is designed to be as minimal as possible, and have the tokens maintain
 * a 1 token == $1 peg at all times. This is a stablecoin with the properties:
 * - Exogenously Collateralized
 * - Dollar Pegged
 * - Algorithmically Stable
 *
 * It is similar to DAI if DAI had no governance, no fees, and was backed by only
 * WETH and WBTC.
 *
 * Our DSC system should always be "overcollateralized".
 *
 * @notice This contract is the core of the Decentralized Stablecoin system.
 * It handles all the logic for minting and redeeming DSC, as well as depositing
 * and withdrawing collateral.
 * @notice This contract is based on the MakerDAO DSS system
 */

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {DecentralizedStableCoin} from "./DecentralizedStableCoin.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import {OracleLib} from "./libraries/OracleLib.sol";

contract DSCEngine is ReentrancyGuard {
    error DSCEngine__TokenAddressesAndPriceFeedAddressesAmountsDontMatch();
    error DSCEngine__NeedsMoreThanZero();
    error DSCEngine__NotAllowedToken();
    error DSCEngine__TransferFailed();
    error DSCEngine__BreaksHealthFactor(uint256 healthFactorValue);
    error DSCEngine__MintFailed();
    error DSCEngine__HealthFactorOk();
    error DSCEngine__HealthFactorNotImproved();

    using OracleLib for AggregatorV3Interface;

    DecentralizedStableCoin private immutable i_dsc;

    uint256 private constant LIQUIDATION_THRESHOLD = 50; // This means you need to be 200% over-collateralized
    uint256 private constant LIQUIDATION_BONUS = 10; // This means liquidator gets assets at a 10% discount when liquidating
    uint256 private constant LIQUIDATION_PRECISION = 100;
    uint256 private constant MIN_HEALTH_FACTOR = 1e18;
    uint256 private constant PRECISION = 1e18;
    uint256 private constant ADDITIONAL_FEED_PRECISION = 1e10;
    uint256 private constant FEED_PRECISION = 1e8;

    /// @dev Mapping of token address to price feed address
    mapping(address collateralToken => address priceFeed) private s_priceFeeds;
    /// @dev Amount of collateral deposited by user
    mapping(address user => mapping(address collateralToken => uint256 amount)) private s_collateralDeposited;
    /// @dev Amount of DSC minted by user
    mapping(address user => uint256 amount) private s_DSCMinted;

    /// @dev If we know exactly how many tokens we have, we could make this immutable!
    address[] private s_collateralTokens;

    event CollateralDeposited(address indexed user, address indexed token, uint256 indexed amount);
    event CollateralRedeemed(address indexed redeemFrom, address indexed redeemTo, address token, uint256 amount);

    modifier moreThanZero(uint256 amount) {
        if (amount == 0) {
            revert DSCEngine__NeedsMoreThanZero();
        }
        _;
    }

    modifier isAllowedToken(address token) {
        if (s_priceFeeds[token] == address(0)) {
            revert DSCEngine__NotAllowedToken();
        }
        _;
    }

    constructor(address[] memory tokenAddresses, address[] memory priceFeedAddresses, address dscAddress) {
        if (tokenAddresses.length != priceFeedAddresses.length) {
            revert DSCEngine__TokenAddressesAndPriceFeedAddressesAmountsDontMatch();
        }

        // For Example ETH / USD, BTC / USD, MKR / USD, etc
        for (uint256 i = 0; i < tokenAddresses.length; i++) {
            s_priceFeeds[tokenAddresses[i]] = priceFeedAddresses[i];
            s_collateralTokens.push(tokenAddresses[i]);
        }

        i_dsc = DecentralizedStableCoin(dscAddress);
    }

    /*
     * @param tokenCollateralAddress: The ERC20 token address of the collateral you're depositing
     * @param amountCollateral: The amount of collateral you're depositing
     * @param amountDscToMint: The amount of DSC you want to mint
     * @notice This function will deposit your collateral and mint DSC in one transaction
     */
    function depositCollateralAndMintDsc(
        address tokenCollateralAddress,
        uint256 amountCollateral,
        uint256 amountDscToMint
    ) external {
        depositCollateral(tokenCollateralAddress, amountCollateral);
        mintDsc(amountDscToMint);
    }

    function getUsdValue(
        address token,
        uint256 amount // in WEI
    ) external view returns (uint256) {
        return _getUsdValue(token, amount);
    }

    /*
     * @notice This function will withdraw your collateral and burn DSC in one transaction
     */
    function redeemCollateralForDsc(address tokenCollateralAddress, uint256 amountCollateral, uint256 amountDscToBurn)
        external
        moreThanZero(amountCollateral)
        isAllowedToken(tokenCollateralAddress)
    {
        _burnDsc(amountDscToBurn, msg.sender, msg.sender);
        _redeemCollateral(tokenCollateralAddress, amountCollateral, msg.sender, msg.sender);
        _revertIfHealthFactorIsBroken(msg.sender);
    }

    function redeemCollateral(address tokenCollateralAddress, uint256 amountCollateral)
        external
        moreThanZero(amountCollateral)
        nonReentrant
        isAllowedToken(tokenCollateralAddress)
    {
        _redeemCollateral(tokenCollateralAddress, amountCollateral, msg.sender, msg.sender);
        _revertIfHealthFactorIsBroken(msg.sender);
    }

    /*
     * @notice careful! You'll burn your DSC here! Make sure you want to do this...
     * @dev you might want to use this if you're nervous you might get liquidated and want to just burn
     * you DSC but keep your collateral in.
     */
    function burnDsc(uint256 amount) external moreThanZero(amount) {
        _burnDsc(amount, msg.sender, msg.sender);
        _revertIfHealthFactorIsBroken(msg.sender); // I don't think this would ever hit...
    }

    function getAccountInformation(address user)
        external
        view
        returns (uint256 totalDscMinted, uint256 collateralValueInUsd)
    {
        totalDscMinted = s_DSCMinted[user];
        collateralValueInUsd = getAccountCollateralValue(user);
    }

    /* This function will be called by liquidator
    * @param collateral: The address of the ERC20 token that is being used as collateral by the user.
    * @param user: The address of the user who is being liquidated.
    * @param debtToCover: The amount of DSC debt that the liquidator is willing to pay off on behalf of the user.
     */
    function liquidate(address collateral, address user, uint256 debtToCover)
        external
        moreThanZero(debtToCover)
        nonReentrant
    {
        uint256 startingUserHealthFactor = _healthFactor(user);
        if (startingUserHealthFactor >= MIN_HEALTH_FACTOR) {
            revert DSCEngine__HealthFactorOk();
        }

        uint256 tokenAmountFromDebtCovered = getTokenAmountFromUsd(collateral, debtToCover);

        // Calculate the liquidation bonus to incentivize liquidators.
        // Example: If `LIQUIDATION_BONUS` is 10% and `tokenAmountFromDebtCovered` is 0.05 ETH,
        // `bonusCollateral` would be 0.05 ETH * 10 / 100 = 0.005 ETH.
        uint256 bonusCollateral = (tokenAmountFromDebtCovered * LIQUIDATION_BONUS) / LIQUIDATION_PRECISION;

        // Redeem the collateral from the user, including the liquidation bonus, and transfer it to the liquidator.
        // Example: The liquidator receives 0.05 ETH + 0.005 ETH = 0.055 ETH in total for covering 100 DSC of debt.
        _redeemCollateral(collateral, tokenAmountFromDebtCovered + bonusCollateral, user, msg.sender);

        // Burn the DSC equivalent to the debt covered by the liquidator.
        _burnDsc(debtToCover, user, msg.sender);

        // Check the user's health factor after liquidation to ensure it has improved.
        uint256 endingUserHealthFactor = _healthFactor(user);
        if (endingUserHealthFactor <= startingUserHealthFactor) {
            revert DSCEngine__HealthFactorNotImproved();
        }

        // Verify the liquidator's own health factor to ensure the system remains stable.
        _revertIfHealthFactorIsBroken(msg.sender);
    }

    function calculateHealthFactor(uint256 totalDscMinted, uint256 collateralValueInUsd)
        external
        pure
        returns (uint256)
    {
        // If the user hasn't minted any DSC (totalDscMinted == 0),
        // they have no debt, so their health factor should be treated as maximally positive.
        // Return the maximum possible uint256 value to represent an "infinite" health factor.
        // This is for avoiding divizion by zero
        if (totalDscMinted == 0) return type(uint256).max;
        // Example: LIQUIDATION_THRESHOLD is 50 (50%), so we consider 50% of the collateral.
        // If collateralValueInUsd is 200, then collateralAdjustedForThreshold = 200 * 50 / 100 = 100.
        uint256 collateralAdjustedForThreshold = (collateralValueInUsd * LIQUIDATION_THRESHOLD) / LIQUIDATION_PRECISION;

        // Example: If totalDscMinted is 100 and collateralAdjustedForThreshold is 100,
        // then healthFactor = (100 * 1e18) / 100 = 1e18 (which is the fixed-point representation of 1).
        return (collateralAdjustedForThreshold * PRECISION) / totalDscMinted;
    }

    /*
     * @param tokenCollateralAddress: The ERC20 token address of the collateral you're depositing
     * @param amountCollateral: The amount of collateral you're depositing
     */
    function depositCollateral(address tokenCollateralAddress, uint256 amountCollateral)
        public
        moreThanZero(amountCollateral)
        isAllowedToken(tokenCollateralAddress)
        nonReentrant
    {
        // Increase the amount of collateral deposited by the user for the specified token.
        s_collateralDeposited[msg.sender][tokenCollateralAddress] += amountCollateral;

        // Emit an event to log the deposit of collateral by the user.
        emit CollateralDeposited(msg.sender, tokenCollateralAddress, amountCollateral);

        // Transfer the specified amount of collateral from the user's address to this contract.
        bool success = IERC20(tokenCollateralAddress).transferFrom(msg.sender, address(this), amountCollateral);

        if (!success) {
            revert DSCEngine__TransferFailed();
        }
    }

    /*
     * @param amountDscToMint: The amount of DSC you want to mint
     * You can only mint DSC if you hav enough collateral
     */
    function mintDsc(uint256 amountDscToMint) public moreThanZero(amountDscToMint) nonReentrant {
        s_DSCMinted[msg.sender] += amountDscToMint;
        _revertIfHealthFactorIsBroken(msg.sender);
        bool minted = i_dsc.mint(msg.sender, amountDscToMint);
        if (!minted) {
            revert DSCEngine__MintFailed();
        }
    }

    function getAccountCollateralValue(address user) public view returns (uint256 totalCollateralValueInUsd) {
        totalCollateralValueInUsd = 0;
        for (uint256 index = 0; index < s_collateralTokens.length; index++) {
            address token = s_collateralTokens[index]; // Get the address of the collateral token.
            uint256 amount = s_collateralDeposited[user][token]; // Get the amount of this token the user has deposited.
            totalCollateralValueInUsd += _getUsdValue(token, amount); // Add the USD value of the token to the total.
        }

        // Example result: If the user has $2000 worth of ETH and $3000 worth of BTC,
        // totalCollateralValueInUsd = 2000 + 3000 = $5000.
        return totalCollateralValueInUsd;
    }

    function getTokenAmountFromUsd(address token, uint256 usdAmountInWei) public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(s_priceFeeds[token]);

        // Fetches the latest price from the Chainlink price feed.
        // Example: If the price feed returns $2000 for ETH, `price` will be 2000 * 10^8 (with 8 decimals).
        (, int256 price,,,) = priceFeed.latestRoundData();

        // This line converts a USD amount (in wei) into the equivalent amount of a token.
        // `usdAmountInWei` is the amount of USD in wei, and `price` is the token price in USD from Chainlink, with 8 decimals.

        // Example:
        // - `usdAmountInWei = 100 * 10^18` (representing $100 in wei)
        // - `price = 2000 * 10^8` (price of 1 ETH = $2000, with 8 decimals)
        // - `PRECISION = 10^18` (to maintain 18 decimals precision)
        // - `ADDITIONAL_FEED_PRECISION = 10^10` (to convert Chainlink price to 18 decimals)

        // Calculation:
        // - Denominator: `price * ADDITIONAL_FEED_PRECISION = 2000 * 10^18`
        // - Numerator: `usdAmountInWei * PRECISION = 100 * 10^36`
        // - Result: `(100 * 10^36) / (2000 * 10^18) = 0.05 * 10^18`
        // This means $100 would convert to 0.05 ETH (if ETH = $2000).
        return ((usdAmountInWei * PRECISION) / (uint256(price) * ADDITIONAL_FEED_PRECISION));
    }

    function _revertIfHealthFactorIsBroken(address user) internal view {
        uint256 userHealthFactor = _healthFactor(user);
        if (userHealthFactor < MIN_HEALTH_FACTOR) {
            revert DSCEngine__BreaksHealthFactor(userHealthFactor);
        }
    }

    function _redeemCollateral(address tokenCollateralAddress, uint256 amountCollateral, address from, address to)
        private
    {
        s_collateralDeposited[from][tokenCollateralAddress] -= amountCollateral;
        emit CollateralRedeemed(from, to, tokenCollateralAddress, amountCollateral);
        // Transfer the specified amount of collateral from the contract to the `to` address.
        bool success = IERC20(tokenCollateralAddress).transfer(to, amountCollateral);
        if (!success) {
            revert DSCEngine__TransferFailed();
        }
    }

    function _burnDsc(uint256 amountDscToBurn, address onBehalfOf, address liquidator) private {
        s_DSCMinted[onBehalfOf] -= amountDscToBurn;
        bool success = i_dsc.transferFrom(liquidator, address(this), amountDscToBurn);
        if (!success) {
            revert DSCEngine__TransferFailed();
        }
        i_dsc.burn(amountDscToBurn);
    }

    /*
    * @notice Returns how close to liquidation a user is.
    * If a user goes below 1, then they can get liquidated.
    * The health factor is a measure of a user's financial health in the system.
    * A health factor > 1 means the user is sufficiently collateralized.
    * A health factor = 1 means the user is on the edge of being under-collateralized.
    * A health factor < 1 means the user is under-collateralized and at risk of liquidation.
    */
    function _healthFactor(address user) private view returns (uint256) {
        uint256 totalDscMinted = s_DSCMinted[user];
        uint256 collateralValueInUsd = getAccountCollateralValue(user);

        // If the user hasn't minted any DSC (totalDscMinted == 0),
        // they have no debt, so their health factor should be treated as maximally positive.
        // Return the maximum possible uint256 value to represent an "infinite" health factor.
        // This is for avoiding divizion by zero
        if (totalDscMinted == 0) return type(uint256).max;
        // Example: LIQUIDATION_THRESHOLD is 50 (50%), so we consider 50% of the collateral.
        // If collateralValueInUsd is 200, then collateralAdjustedForThreshold = 200 * 50 / 100 = 100.
        uint256 collateralAdjustedForThreshold = (collateralValueInUsd * LIQUIDATION_THRESHOLD) / LIQUIDATION_PRECISION;

        // Example: If totalDscMinted is 100 and collateralAdjustedForThreshold is 100,
        // then healthFactor = (100 * 1e18) / 100 = 1e18 (which is the fixed-point representation of 1).
        return (collateralAdjustedForThreshold * PRECISION) / totalDscMinted;
    }

    function _getUsdValue(address token, uint256 amount) private view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(s_priceFeeds[token]);
        (, int256 price,,,) = priceFeed.staleCheckLatestRoundData();
        // 1 ETH = 1000 USD
        // The returned value from Chainlink will be 1000 * 1e8
        // Most USD pairs have 8 decimals, so we will just pretend they all do.
        // We want to have everything in terms of WEI, so we add 10 zeros at the end
        return ((uint256(price) * ADDITIONAL_FEED_PRECISION) * amount) / PRECISION;
    }

    function getPrecision() external pure returns (uint256) {
        return PRECISION;
    }

    function getAdditionalFeedPrecision() external pure returns (uint256) {
        return ADDITIONAL_FEED_PRECISION;
    }

    function getLiquidationThreshold() external pure returns (uint256) {
        return LIQUIDATION_THRESHOLD;
    }

    function getLiquidationBonus() external pure returns (uint256) {
        return LIQUIDATION_BONUS;
    }

    function getLiquidationPrecision() external pure returns (uint256) {
        return LIQUIDATION_PRECISION;
    }

    function getMinHealthFactor() external pure returns (uint256) {
        return MIN_HEALTH_FACTOR;
    }

    function getCollateralTokens() external view returns (address[] memory) {
        return s_collateralTokens;
    }

    function getDsc() external view returns (address) {
        return address(i_dsc);
    }

    function getCollateralTokenPriceFeed(address token) external view returns (address) {
        return s_priceFeeds[token];
    }

    function getHealthFactor(address user) external view returns (uint256) {
        return _healthFactor(user);
    }

    function getCollateralBalanceOfUser(address user, address token) external view returns (uint256) {
        return s_collateralDeposited[user][token];
    }
}
