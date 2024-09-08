// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

// // Invariants:
// // protocol must never be insolvent / undercollateralized
// // users cant create stablecoins with a bad health factor
// // a user should only be able to be liquidated if they have a bad health factor

import {Test, console} from "forge-std/Test.sol";
import {StdInvariant} from "forge-std/StdInvariant.sol";
import {DSCEngine} from "../../src/DSCEngine.sol";
import {DecentralizedStableCoin} from "../../src/DecentralizedStableCoin.sol";
import {HelperConfig} from "../../script/HelperConfig.s.sol";
import {DeployDSC} from "../../script/DeployDSC.s.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {Handler} from "./Handler.t.sol";

contract InvariantTest is StdInvariant, Test {
    DeployDSC deployer;
    DSCEngine dsce;
    DecentralizedStableCoin dsc;
    HelperConfig helperConfig;
    address weth;
    address wbtc;
    Handler handler;

    function setUp() external {
        deployer = new DeployDSC();
        (dsc, dsce, helperConfig) = deployer.run();
        (,, weth, wbtc) = helperConfig.activeNetworkConfig();
        handler = new Handler(dsce, dsc);
        targetContract(address(handler));
    }

    function invariant_protocolMustHaveMoreValueThanTotalSupply() public view {
        // Get the total supply of the stablecoin (DSC) that has been minted and is in circulation.
        // For example, if 1000 DSC has been minted, totalSupply will be 1000.
        uint256 totalSupply = dsc.totalSupply();

        // Get the total amount of WETH deposited in the DSCEngine contract.
        // For example, if users have deposited 50 WETH in the contract, totalWethDeposited will be 50.
        uint256 totalWethDeposited = IERC20(weth).balanceOf(address(dsce));

        // Get the total amount of WBTC deposited in the DSCEngine contract.
        // For example, if users have deposited 20 WBTC in the contract, totalWbtcDeposited will be 20.
        uint256 totalWbtcDeposited = IERC20(wbtc).balanceOf(address(dsce));

        // Convert the total WETH deposited into its USD value using the price feed in DSCEngine.
        // For example, if 1 WETH is worth $2000 and 50 WETH are deposited, wethValue will be $100,000.
        uint256 wethValue = dsce.getUsdValue(weth, totalWethDeposited);

        // Convert the total WBTC deposited into its USD value using the price feed in DSCEngine.
        // For example, if 1 WBTC is worth $30,000 and 20 WBTC are deposited, wbtcValue will be $600,000.
        uint256 wbtcValue = dsce.getUsdValue(wbtc, totalWbtcDeposited);

        console.log("wethValue: %s", wethValue);
        console.log("wbtcValue: %s", wbtcValue);
        console.log("total supply: %s", totalSupply);

        // Assert that the total value of WETH and WBTC in USD is greater than or equal to the total DSC supply.
        // This ensures that the protocol is overcollateralized.
        assert(wethValue + wbtcValue >= totalSupply);
    }
}