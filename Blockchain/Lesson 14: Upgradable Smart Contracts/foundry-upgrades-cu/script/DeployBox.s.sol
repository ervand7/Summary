// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import {Script} from "forge-std/Script.sol";
import {BoxV1} from "../src/BoxV1.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";

contract DeployBox is Script {
    function run() external returns (address) {
        address proxy = deployBox();
        return proxy;
    }

    function deployBox() public returns (address) {
        vm.startBroadcast();
        BoxV1 box = new BoxV1(); // implementation
        // creating proxy contract
        ERC1967Proxy proxy = new ERC1967Proxy(address(box), "");

        // Casting the proxy contract's address to the BoxV1 type so that we can call 
        // the initialize() function on it. Even though the proxy is an instance of 
        // ERC1967Proxy, it delegates function calls to the BoxV1 implementation contract.
        // The initialize() function is used instead of a constructor to set up ownership 
        // and UUPS upgradeability in upgradeable contracts.
        BoxV1(address(proxy)).initialize();

        vm.stopBroadcast();
        return address(proxy);
    }
}
