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
    /*//////////////////////////////////////////////////////////////
                                 ERRORS
    //////////////////////////////////////////////////////////////*/
    error MinimalAccount__NotFromEntryPoint();
    error MinimalAccount__NotFromEntryPointOrOwner();
    error MiniamlAccount__CallFailed(bytes);

    /*//////////////////////////////////////////////////////////////
                            STATE VARIABLES
    //////////////////////////////////////////////////////////////*/
    IEntryPoint private immutable i_entryPoint;

    /*//////////////////////////////////////////////////////////////
                               MODIFIERS
    //////////////////////////////////////////////////////////////*/
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

    /*//////////////////////////////////////////////////////////////
                               FUNCTIONS
    //////////////////////////////////////////////////////////////*/
    constructor(address entryPoint) Ownable(msg.sender) {
        i_entryPoint = IEntryPoint(entryPoint);
    }

    receive() external payable {}

    /*//////////////////////////////////////////////////////////////
                           EXTERNAL FUNCTIONS
    //////////////////////////////////////////////////////////////*/
    function execute(address dest, uint256 value, bytes calldata functionData) external requireFromEntryPointOrOwner {
        // 1. Perform a low-level call to the `dest` (destination) address.
        //    `dest.call{value: value}(functionData)` sends `value` amount of native currency (e.g., ETH)
        //    and executes the function call defined by `functionData` on the `dest` address.
        //    The `call` function is used for flexible external function execution.
        //    The call returns two values:
        //    - `success`: a boolean indicating whether the call was successful or not.
        //    - `result`: the returned data (if any) from the called function.
        (bool success, bytes memory result) = dest.call{value: value}(functionData);

        // 2. Check if the external call was unsuccessful (`success == false`).
        //    If the call failed, revert the transaction and provide an error message.
        //    `result` contains the reason for the failure, which is returned as part of the custom error `MiniamlAccount__CallFailed`.
        if (!success) {
            revert MiniamlAccount__CallFailed(result);
        }
    }

    // A signature is valid, if it's the MinimalAccount owner
    function validateUserOp(PackedUserOperation calldata userOp, bytes32 userOpHash, uint256 missingAccountFunds)
        external
        requireFromEntryPoint
        returns (uint256 validationData)
    {
        // `userOp` is the packed data of the user's operation that needs to be processed.
        // It includes important information like the sender's address, signature, nonce, and call data.
        // This is passed as `calldata` to optimize gas usage as it only needs to be read, not modified.

        // `userOpHash` is the hash of the entire user operation.
        // This hash is used to verify the integrity and authenticity of the operation.
        // The hash is passed as a separate argument to avoid recalculating it inside the function.

        // `missingAccountFunds` represents the amount of funds that are needed to cover the transaction costs.
        // If the account does not have enough balance to cover gas fees, this value indicates how much more is required.

        // Validate the user's signature using the `userOp` and `userOpHash`.
        validationData = _validateSignature(userOp, userOpHash);

        // Pay any missing funds required to ensure the transaction can proceed.
        _payPrefund(missingAccountFunds);
    }

    /*//////////////////////////////////////////////////////////////
                           INTERNAL FUNCTIONS
    //////////////////////////////////////////////////////////////*/
    // EIP-191 version of the signed hash
    function _validateSignature(PackedUserOperation calldata userOp, bytes32 userOpHash)
        internal
        view
        returns (uint256 validationData)
    {
        // 1. Convert the `userOpHash` into an Ethereum Signed Message Hash format.
        //    This is the EIP-191 specification, where the hash is prefixed with "\x19Ethereum Signed Message:\n32" before hashing.
        bytes32 ethSignedMessageHash = MessageHashUtils.toEthSignedMessageHash(userOpHash);

        // 2. Recover the signer's address from the signature provided in `userOp.signature`.
        //    It uses the ECDSA (Elliptic Curve Digital Signature Algorithm) to recover the signer
        //    from the `ethSignedMessageHash` and the `userOp.signature`.
        address signer = ECDSA.recover(ethSignedMessageHash, userOp.signature);

        // 3. Check if the recovered signer's address is the contract owner.
        //    The owner is the only valid signer for this contract.
        //    If the recovered signer is not the owner, return `SIG_VALIDATION_FAILED`.
        if (signer != owner()) {
            return SIG_VALIDATION_FAILED;
        }

        // 4. If the signer is the contract owner, return `SIG_VALIDATION_SUCCESS`, indicating the signature is valid.
        return SIG_VALIDATION_SUCCESS;
    }

    function _payPrefund(uint256 missingAccountFunds) internal {
        // 1. Check if there are any missing funds that the account needs to cover.
        //    If `missingAccountFunds` is non-zero, it means the account doesn't have enough funds to
        //    cover the gas fees or other costs required for the transaction.
        if (missingAccountFunds != 0) {
            // 2. Initiate a payment of the `missingAccountFunds` from the current contract to the caller (`msg.sender`).
            //    The caller is typically the `EntryPoint` contract that facilitates user operations.
            //    The payable call sends the specified `missingAccountFunds` value to `msg.sender`.
            //    The `gas: type(uint256).max` ensures that the transaction uses the maximum possible gas to succeed.
            (bool success,) = payable(msg.sender).call{value: missingAccountFunds, gas: type(uint256).max}("");

            // 3. Evaluate the success of the transfer operation.
            //    This line simply evaluates the result of the `call`, ensuring the code compiles
            //    without issuing warnings about unused variables.
            (success); // This line ignores the `success` value but ensures it is evaluated for any warnings.
        }
    }

    /*//////////////////////////////////////////////////////////////
                                GETTERS
    //////////////////////////////////////////////////////////////*/
    function getEntryPoint() external view returns (address) {
        return address(i_entryPoint);
    }
}
