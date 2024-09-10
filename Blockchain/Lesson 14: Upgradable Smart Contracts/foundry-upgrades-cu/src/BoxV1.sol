// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import {OwnableUpgradeable} from "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";
import {Initializable} from "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import {UUPSUpgradeable} from "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";

contract BoxV1 is Initializable, OwnableUpgradeable, UUPSUpgradeable {
    uint256 internal value;

    /// @custom:oz-upgrades-unsafe-allow constructor
    // A custom tag added for documentation purposes. This informs users that the
    // constructor is allowed in this upgradeable contract despite OpenZeppelin's
    // recommendation to avoid constructors in upgradeable contracts.

    constructor() {
        // ensuring that the contract cannot be initialized by anyone after deployment
        // (since upgradeable contracts use initializer functions instead of constructors).
        _disableInitializers();
    }

    function initialize() public initializer {
        __Ownable_init();
        // This function is part of the OwnableUpgradeable contract from OpenZeppelin.
        // It initializes the contract's ownership functionality by setting the
        // deployer (or the caller of the `initialize` function) as the initial
        // owner of the contract.
        // Since upgradeable contracts don't use constructors, this ensures ownership logic is properly initialized.

        // This function is part of the UUPSUpgradeable contract from OpenZeppelin.
        // It initializes the necessary internal variables and settings for UUPS upgradeable functionality,
        // allowing this contract to be upgraded in the future using the UUPS proxy pattern.
        __UUPSUpgradeable_init();
    }

    function getValue() public view returns (uint256) {
        return value;
    }

    function version() public pure returns (uint256) {
        return 1;
    }

    function _authorizeUpgrade(address newImplementation) internal override onlyOwner {}
}
