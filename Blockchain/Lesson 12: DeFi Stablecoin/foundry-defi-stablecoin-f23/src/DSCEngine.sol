// Layout of Contract:
// version
// imports
// errors
// interfaces, libraries, contracts
// Type declarations
// State variables
// Events
// Modifiers
// Functions

// Layout of Functions:
// constructor
// receive function (if exists)
// fallback function (if exists)
// external
// public
// internal
// private
// internal & private view & pure functions
// external & public view & pure functions

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
 * Our DSC system should always be "overcollateralized". At no point, should the value of
 * all collateral < the $ backed value of all the DSC.
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

contract DSCEngine is ReentrancyGuard {
    ///////////////////
    // Errors
    ///////////////////
    error DSCEngine__TokenAddressesAndPriceFeedAddressesAmountsDontMatch();
    error DSCEngine__NeedsMoreThanZero();
    error DSCEngine__NotAllowedToken();
    error DSCEngine__TransferFailed();
    error DSCEngine__BreaksHealthFactor(uint256 healthFactorValue);
    error DSCEngine__MintFailed();
    error DSCEngine__HealthFactorOk();
    error DSCEngine__HealthFactorNotImproved();

    ///////////////////
    // State Variables
    ///////////////////
    DecentralizedStableCoin private immutable i_dsc;

    uint256 private constant LIQUIDATION_THRESHOLD = 50; // This means you need to be 200% over-collateralized
    uint256 private constant LIQUIDATION_BONUS = 10; // This means you get assets at a 10% discount when liquidating
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

    ///////////////////
    // Events
    ///////////////////
    event CollateralDeposited(address indexed user, address indexed token, uint256 indexed amount);
    // if redeemFrom != redeemedTo, then it was liquidated
    event CollateralRedeemed(address indexed redeemFrom, address indexed redeemTo, address token, uint256 amount);

    ///////////////////
    // Modifiers
    ///////////////////
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

    ///////////////////
    // Functions
    ///////////////////
    constructor(address[] memory tokenAddresses, address[] memory priceFeedAddresses, address dscAddress) {
        // USD Price Feeds
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

    ///////////////////
    // External Functions
    ///////////////////
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
     * @param tokenCollateralAddress: The ERC20 token address of the collateral you're depositing
     * @param amountCollateral: The amount of collateral you're depositing
     * @param amountDscToBurn: The amount of DSC you want to burn
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

    /*
    In order to redeem collateral:
    1. Health factor must be over 1 AFTER collateral pulled
     * @param tokenCollateralAddress: The ERC20 token address of the collateral you're redeeming
     * @param amountCollateral: The amount of collateral you're redeeming
     * @notice This function will redeem your collateral.
     * @notice If you have DSC minted, you will not be able to redeem until you burn your DSC
     */
    function redeemCollateral(address tokenCollateralAddress, uint256 amountCollateral)
        external
        moreThanZero(amountCollateral)
        nonReentrant
        isAllowedToken(tokenCollateralAddress)
    {
        // The `msg.sender` is passed twice to the `_redeemCollateral` function because:
        // 1. The first `msg.sender` represents the `from` address, indicating the user who is redeeming the collateral.
        // 2. The second `msg.sender` represents the `to` address, indicating the same user should receive the collateral back.
        // This approach is flexible and allows for scenarios where `from` and `to` might differ, such as in liquidation processes,
        // but in this case, the user redeeming the collateral is also the recipient.
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

    /*
    ### Зачем нужна функция ликвидации?
    Функция ликвидации защищает систему от рисков, когда у пользователя недостаточно залога для покрытия 
    его долга. Ликвидатор (другой пользователь) может покрыть этот долг в обмен на залог пользователя и 
    получить за это бонус.

    ### Что происходит в функции по шагам:

    1. **Проверка здоровья пользователя:**
    - Строка `uint256 startingUserHealthFactor = _healthFactor(user);`
    - Мы проверяем, насколько "здоров" пользователь, т.е. хватает ли у него залога для покрытия долга. 
    Если его "здоровье" выше минимального значения (`MIN_HEALTH_FACTOR`), ликвидация не требуется.

    2. **Если пользователь здоров, то операция отменяется:**
    - Строка `if (startingUserHealthFactor >= MIN_HEALTH_FACTOR) { revert DSCEngine__HealthFactorOk(); }`
    - Если у пользователя достаточно залога, операция ликвидации прерывается.

    3. **Вычисление залога для покрытия долга:**
    - Строка `uint256 tokenAmountFromDebtCovered = getTokenAmountFromUsd(collateral, debtToCover);`
    - Мы считаем, сколько залога нужно забрать у пользователя, чтобы покрыть его долг. Например, если 
    долг 100 DSC, и залог — это ETH, мы определяем, сколько ETH нужно забрать.

    4. **Добавление бонуса ликвидатору:**
    - Строка `uint256 bonusCollateral = (tokenAmountFromDebtCovered * LIQUIDATION_BONUS) / LIQUIDATION_PRECISION;`
    - Ликвидатор получает бонус (например, 10%) к залогу за участие в ликвидации. Это стимулирует 
    пользователей выполнять ликвидации.

    5. **Перевод залога ликвидатору:**
    - Строка `_redeemCollateral(collateral, tokenAmountFromDebtCovered + bonusCollateral, user, msg.sender);`
    - Рассчитанная сумма залога, включая бонус, переводится от пользователя к ликвидатору. Ликвидатор 
    получает залог, покрывая долг пользователя.

    6. **Сжигание долга:**
    - Строка `_burnDsc(debtToCover, user, msg.sender);`
    - Система сжигает (удаляет) количество DSC, эквивалентное долгу, чтобы уменьшить долг пользователя 
    перед системой.

    7. **Проверка здоровья после ликвидации:**
    - Строка `uint256 endingUserHealthFactor = _healthFactor(user);`
    - Мы снова проверяем "здоровье" пользователя после ликвидации. Если оно не улучшилось, операция 
    отменяется.

    8. **Если здоровье не улучшилось, то операция отменяется:**
    - Строка `if (endingUserHealthFactor <= startingUserHealthFactor) { revert DSCEngine__HealthFactorNotImproved(); }`
    - Если после ликвидации здоровье пользователя не улучшилось, значит что-то пошло не так, и операция 
    отменяется.

    9. **Проверка здоровья ликвидатора:**
    - Строка `_revertIfHealthFactorIsBroken(msg.sender);`
    - Проверяем, что ликвидатор сам остаётся "здоровым" после операции, чтобы он не оказался в плохом 
    положении после ликвидации.

    ### Зачем всё это нужно?
    Эта функция защищает систему от рисков и обесценивания активов, когда кто-то не может вернуть свои 
    долги. Ликвидаторы помогают поддерживать баланс в системе и получают за это вознаграждение.


    ПОДРОБНЕЕ ПРО ЛИКВИДАЦИЮ:
    ### Как это работает:
    - **Долг:** Пользователь занимает DSC под залог ETH. Например, пользователь взял 100 DSC под залог 1 ETH.
    - **Ликвидация:** Если стоимость залога падает, и у пользователя становится недостаточно залога для покрытия 
    долга (его health factor падает ниже минимального), система позволяет ликвидаторам погасить его долг.
    - **Что делает ликвидатор:** Ликвидатор погашает, например, 100 DSC долга за пользователя. Взамен он получает 
    эквивалентную сумму залога пользователя в ETH, плюс бонус (например, 10%).
    - **Результат:** Ликвидатор погашает долг (DSC) и получает залог (ETH) с бонусом, а пользователь теряет часть 
    своего залога.

    ### Еще:
    1. **Погашение долга:** Ликвидатор использует свои DSC, чтобы погасить долг пользователя в системе. 
    Эти DSC снимаются с баланса ликвидатора.
    2. **Сжигание DSC:** Система уничтожает (сжигает) эти DSC, чтобы уменьшить общий объём выпущенных 
    стабильных монет. Это означает, что после ликвидации эти DSC больше не существуют в системе.
    3. **Получение залога:** Взамен ликвидатор получает часть залога пользователя (например, ETH) и бонус 
    в виде дополнительного залога.


     * @param collateral: The address of the ERC20 token that is being used as collateral by the user.
    * This is the type of asset that will be taken from the user if they are being liquidated.
    *
    * @param user: The address of the user who is being liquidated. This user has a health factor below
    * the minimum required, meaning they don’t have enough collateral to cover their debt.
    *
    * @param debtToCover: The amount of DSC (Decentralized Stable Coin) debt that the liquidator is willing
    * to pay off on behalf of the user. In exchange for covering this debt, the liquidator will receive 
    * some of the user’s collateral, along with a bonus.
     */
    function liquidate(address collateral, address user, uint256 debtToCover)
        external
        moreThanZero(debtToCover)
        nonReentrant
    {
        // Fetch the user's current health factor before liquidation.
        uint256 startingUserHealthFactor = _healthFactor(user);

        // If the user's health factor is above the minimum (not eligible for liquidation), revert the transaction.
        if (startingUserHealthFactor >= MIN_HEALTH_FACTOR) {
            revert DSCEngine__HealthFactorOk();
        }

        // Calculate the amount of collateral equivalent to the debt being covered.
        // Example: If `debtToCover` is 100 DSC and the collateral is ETH priced at $2000,
        // `tokenAmountFromDebtCovered` would be 100 DSC * 1 ETH / 2000 DSC = 0.05 ETH.
        uint256 tokenAmountFromDebtCovered = getTokenAmountFromUsd(collateral, debtToCover);

        // Calculate the liquidation bonus to incentivize liquidators.
        // Example: If `LIQUIDATION_BONUS` is 10% and `tokenAmountFromDebtCovered` is 0.05 ETH,
        // `bonusCollateral` would be 0.05 ETH * 10 / 100 = 0.005 ETH.
        uint256 bonusCollateral = (tokenAmountFromDebtCovered * LIQUIDATION_BONUS) / LIQUIDATION_PRECISION;

        // Redeem the collateral from the user, including the liquidation bonus, and transfer it to the liquidator.
        // Example: The liquidator receives 0.05 ETH + 0.005 ETH = 0.055 ETH in total for covering 100 DSC of debt.
        _redeemCollateral(collateral, tokenAmountFromDebtCovered + bonusCollateral, user, msg.sender);

        // Burn the DSC equivalent to the debt covered by the liquidator.
        // Example: The liquidator's 100 DSC is burned to reduce the user's debt.
        _burnDsc(debtToCover, user, msg.sender);

        // Check the user's health factor after liquidation to ensure it has improved.
        uint256 endingUserHealthFactor = _healthFactor(user);

        // If the user's health factor hasn't improved, something went wrong, so revert the transaction.
        if (endingUserHealthFactor <= startingUserHealthFactor) {
            revert DSCEngine__HealthFactorNotImproved();
        }

        // Verify the liquidator's own health factor to ensure the system remains stable.
        _revertIfHealthFactorIsBroken(msg.sender);
    }

    function getHealthFactor() external view {}

    ///////////////////
    // Public Functions
    ///////////////////
    /*
     * @param tokenCollateralAddress: The ERC20 token address of the collateral you're depositing
     * @param amountCollateral: The amount of collateral you're depositing
     */
    function depositCollateral(address tokenCollateralAddress, uint256 amountCollateral)
        public
        moreThanZero(amountCollateral) // Ensure the amount of collateral is more than zero using the modifier.
        isAllowedToken(tokenCollateralAddress) // Ensure the token is allowed as collateral using the modifier.
        nonReentrant // Prevent reentrancy attacks using the modifier.
    {
        // Increase the amount of collateral deposited by the user for the specified token.
        s_collateralDeposited[msg.sender][tokenCollateralAddress] += amountCollateral;

        // Emit an event to log the deposit of collateral by the user.
        emit CollateralDeposited(msg.sender, tokenCollateralAddress, amountCollateral);

        // Transfer the specified amount of collateral from the user's address to this contract.
        bool success = IERC20(tokenCollateralAddress).transferFrom(msg.sender, address(this), amountCollateral);

        // If the transfer fails, revert the transaction with a custom error.
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

    /*
    * @notice Calculates the total value of a user's collateral in USD.
    * This function sums up the value of all collateral tokens deposited by the user.
    */
    function getAccountCollateralValue(address user) public view returns (uint256 totalCollateralValueInUsd) {
        // Initialize the total collateral value in USD to 0.
        totalCollateralValueInUsd = 0; // Example: Start with $0 as the total collateral value.

        // Iterate over all collateral tokens the system supports.
        for (uint256 index = 0; index < s_collateralTokens.length; index++) {
            address token = s_collateralTokens[index]; // Get the address of the collateral token.

            // Example: Suppose the user has 1 ETH and 0.1 BTC as collateral.
            uint256 amount = s_collateralDeposited[user][token]; // Get the amount of this token the user has deposited.

            // Example: If 1 ETH is worth $2000, and the user has 1 ETH, _getUsdValue will return $2000.
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

    //////////////////////////////
    // Internal & Private & View & Pure Functions
    //////////////////////////////

    // 1. Check health factor (do they have enougth collateral?)
    // 2. Revert if they don't
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
        // This is used when a user redeems their collateral, moving the tokens back to their wallet.
        // The transfer must succeed, otherwise, the transaction will revert with a custom error.
        bool success = IERC20(tokenCollateralAddress).transfer(to, amountCollateral);
        if (!success) {
            revert DSCEngine__TransferFailed();
        }
    }

    function _burnDsc(uint256 amountDscToBurn, address onBehalfOf, address dscFrom) private {
        // Reduce the record of DSC minted by the user (`onBehalfOf`) by the amount specified.
        s_DSCMinted[onBehalfOf] -= amountDscToBurn;

        // Attempt to transfer the specified amount of DSC from the `dscFrom` address to this contract.
        // Why: Before we can burn DSC, the tokens need to be in the contract's possession. This transfer
        // effectively moves the tokens from the user back into the contract, preparing them for burning.
        bool success = i_dsc.transferFrom(dscFrom, address(this), amountDscToBurn);

        if (!success) {
            revert DSCEngine__TransferFailed();
        }

        // Burn the specified amount of DSC that was successfully transferred to this contract.
        // Why: Burning the DSC tokens permanently removes them from circulation, reducing the total supply.
        // This is typically done to reduce the user's debt within the system or to correct the total DSC supply.
        // After this step, the tokens no longer exist, which aligns with the goal of reducing the user's liability.
        i_dsc.burn(amountDscToBurn);
    }

    /*
    * @notice Retrieves the total DSC minted by the user and the total value of the user's collateral in USD.
    * This information is used to assess the user's financial health in the system.
    */
    function _getAccountInformation(address user)
        private
        view
        returns (uint256 totalDscMinted, uint256 collateralValueInUsd)
    {
        // Example: Suppose the user has minted 100 DSC.
        totalDscMinted = s_DSCMinted[user]; // Get the total amount of DSC minted by the user.

        // Example: Suppose the user has deposited 1 ETH and 0.1 BTC as collateral.
        // The getAccountCollateralValue function would convert these amounts to their USD equivalents.
        collateralValueInUsd = getAccountCollateralValue(user); // Get the total value of the user's collateral in USD.

        // Example result: If the user has minted 100 DSC and their collateral is worth $200,
        // totalDscMinted = 100, collateralValueInUsd = 200.
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
        // Example: Suppose the user has minted 100 DSC and their collateral is worth $200 in total.
        (uint256 totalDscMinted, uint256 collateralValueInUsd) = _getAccountInformation(user);

        // Example: LIQUIDATION_THRESHOLD is 50 (50%), so we consider 50% of the collateral.
        // If collateralValueInUsd is 200, then collateralAdjustedForThreshold = 200 * 50 / 100 = 100.
        uint256 collateralAdjustedForThreshold = (collateralValueInUsd * LIQUIDATION_THRESHOLD) / LIQUIDATION_PRECISION;

        // Example: If totalDscMinted is 100 and collateralAdjustedForThreshold is 100,
        // then healthFactor = (100 * 1e18) / 100 = 1e18 (which is the fixed-point representation of 1).
        return (collateralAdjustedForThreshold * PRECISION) / totalDscMinted;
    }

    function _getUsdValue(address token, uint256 amount) private view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(s_priceFeeds[token]);
        (, int256 price,,,) = priceFeed.latestRoundData();
        // 1 ETH = 1000 USD
        // The returned value from Chainlink will be 1000 * 1e8
        // Most USD pairs have 8 decimals, so we will just pretend they all do.
        // We want to have everything in terms of WEI, so we add 10 zeros at the end
        return ((uint256(price) * ADDITIONAL_FEED_PRECISION) * amount) / PRECISION;
    }
}
