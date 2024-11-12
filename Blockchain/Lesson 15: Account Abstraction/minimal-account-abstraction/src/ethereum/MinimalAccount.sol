// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import {IAccount} from "lib/account-abstraction/contracts/interfaces/IAccount.sol";
import {PackedUserOperation} from "lib/account-abstraction/contracts/interfaces/PackedUserOperation.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {MessageHashUtils} from "@openzeppelin/contracts/utils/cryptography/MessageHashUtils.sol";
import {ECDSA} from "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import {SIG_VALIDATION_FAILED, SIG_VALIDATION_SUCCESS} from "lib/account-abstraction/contracts/core/Helpers.sol";
import {IEntryPoint} from "lib/account-abstraction/contracts/interfaces/IEntryPoint.sol";

contract MinimalAccount is IAccount, Ownable {
    // ERRORS
    error MinimalAccount__NotFromEntryPoint();
    error MinimalAccount__NotFromEntryPointOrOwner();
    error MiniamlAccount__CallFailed(bytes);

    // STATE VARIABLES
    IEntryPoint private immutable i_entryPoint;

    // MODIFIERS
    modifier requireFromEntryPoint() {
        if (msg.sender != address(i_entryPoint)) {
            revert MinimalAccount__NotFromEntryPoint();
        }
        _;
    }

    modifier requireFromEntryPointOrOwner() {
        if (msg.sender != address(i_entryPoint) && msg.sender != owner()) {
            revert MinimalAccount__NotFromEntryPointOrOwner();
        }
        _;
    }

    // FUNCTIONS
    constructor(address entryPoint) Ownable(msg.sender) {
        i_entryPoint = IEntryPoint(entryPoint);
    }

    receive() external payable {}

    // EXTERNAL FUNCTIONS
    /**
     * @notice Allows the owner or EntryPoint to execute a transaction on behalf
     * of this account.
     * @dev Executes a call to `dest` with the provided `value` and `functionData`.
     * @param dest The destination address to call.
     * @param value The amount of ether to send with the call.
     * @param functionData The calldata to send to the destination address.
     */
    function execute(address dest, uint256 value, bytes calldata functionData) external requireFromEntryPointOrOwner {
        (bool success, bytes memory result) = dest.call{value: value}(functionData);
        if (!success) {
            revert MiniamlAccount__CallFailed(result);
        }
    }

    /**
     * @notice Validates a user operation by verifying the signature and ensuring the
     * account has sufficient funds.
     * @dev This function is called by the EntryPoint contract to validate the user's operation.
     *      It checks the signature against the owner's address and pays any required prefunding.
     *      Only callable by the EntryPoint contract.
     * @param userOp The packed user operation containing details like sender, signature,
     * nonce, and call data.
     * @param userOpHash The hash of the user operation used for signature verification.
     * @param missingAccountFunds The amount of funds needed to cover transaction
     * costs; the account supplies this if required.
     * @return validationData A status code indicating whether the signature is valid or not.
     */
    function validateUserOp(PackedUserOperation calldata userOp, bytes32 userOpHash, uint256 missingAccountFunds)
        external
        requireFromEntryPoint
        returns (uint256 validationData)
    {
        validationData = _validateSignature(userOp, userOpHash);
        _payPrefund(missingAccountFunds);
    }

    // INTERNAL FUNCTIONS
    /**
     * @notice Validates the signature of a user operation to ensure it's authorized by the owner.
     * @dev Converts the user operation hash to an Ethereum Signed Message Hash (per EIP-191),
     *      recovers the signer's address from the signature, and verifies it matches the owner.
     *      Returns a validation status code indicating success or failure.
     * @param userOp The packed user operation containing the signature to verify.
     * @param userOpHash The hash of the user operation used for signature verification.
     * @return validationData Status code indicating signature validation result (success or failure).
     */
    function _validateSignature(PackedUserOperation calldata userOp, bytes32 userOpHash)
        internal
        view
        returns (uint256 validationData)
    {
        bytes32 ethSignedMessageHash = MessageHashUtils.toEthSignedMessageHash(userOpHash);
        address signer = ECDSA.recover(ethSignedMessageHash, userOp.signature);
        if (signer != owner()) {
            return SIG_VALIDATION_FAILED;
        }
        return SIG_VALIDATION_SUCCESS;
    }

    /**
     * @notice Ensures the account provides sufficient funds to cover transaction costs.
     * @dev If the EntryPoint contract indicates that the account is missing funds (`missingAccountFunds > 0`),
     *      this function transfers the required amount to the EntryPoint.
     *      It uses a payable call with maximum gas to ensure the transfer succeeds.
     * @param missingAccountFunds The amount of ether the account needs to supply to cover transaction costs.
     */
    function _payPrefund(uint256 missingAccountFunds) internal {
        if (missingAccountFunds != 0) {
            (bool success,) = payable(msg.sender).call{value: missingAccountFunds, gas: type(uint256).max}("");
            (success);
        }
    }

    // GETTERS
    function getEntryPoint() external view returns (address) {
        return address(i_entryPoint);
    }
}
