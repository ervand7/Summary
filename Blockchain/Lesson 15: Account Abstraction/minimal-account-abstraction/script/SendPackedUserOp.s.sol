// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import {Script, console2} from "forge-std/Script.sol";
import {PackedUserOperation} from "lib/account-abstraction/contracts/interfaces/PackedUserOperation.sol";
import {HelperConfig} from "script/HelperConfig.s.sol";
import {IEntryPoint} from "lib/account-abstraction/contracts/interfaces/IEntryPoint.sol";
import {MessageHashUtils} from "@openzeppelin/contracts/utils/cryptography/MessageHashUtils.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {MinimalAccount} from "src/ethereum/MinimalAccount.sol";
import {DevOpsTools} from "lib/foundry-devops/src/DevOpsTools.sol";

contract SendPackedUserOp is Script {
    using MessageHashUtils for bytes32;

    // Make sure you trust this user - don't run this on Mainnet!
    address constant RANDOM_APPROVER = 0x9EA9b0cc1919def1A3CfAEF4F7A66eE3c36F86fC;

    function run() public {
        // Setup
        HelperConfig helperConfig = new HelperConfig();
        address dest = helperConfig.getConfig().usdc; // arbitrum mainnet USDC address
        uint256 value = 0;
        address minimalAccountAddress = DevOpsTools.get_most_recent_deployment("MinimalAccount", block.chainid);

        // Encode the calldata for the IERC20 approve function,
        // approving RANDOM_APPROVER to spend 1e18 tokens on behalf of the sender
        bytes memory functionData = abi.encodeWithSelector(
            IERC20.approve.selector, // Function selector for IERC20.approve(address spender, uint256 amount)
            RANDOM_APPROVER, // The address being approved to spend tokens
            1e18 // The amount of tokens to approve (in wei, so 1e18 represents 1 token with 18 decimals)
        );

        // Encode the calldata for the MinimalAccount's execute function,
        // which will execute the approve function on the token contract
        bytes memory executeCalldata = abi.encodeWithSelector(
            MinimalAccount.execute.selector, // Function selector for MinimalAccount.execute(address dest, uint256 value, bytes calldata functionData)
            dest, // The destination address (token contract address where approve will be called)
            value, // Amount of Ether to send with the call (usually 0 for token interactions)
            functionData // The calldata for the approve function encoded above
        );
        PackedUserOperation memory userOp =
            generateSignedUserOperation(executeCalldata, helperConfig.getConfig(), minimalAccountAddress);
        PackedUserOperation[] memory ops = new PackedUserOperation[](1);
        ops[0] = userOp;

        // Send transaction
        vm.startBroadcast();
        // Calls the EntryPoint contract's `handleOps` function, submitting the array of signed UserOperations `ops`.
        // The EntryPoint processes each UserOperation by performing validation and executing the requested actions.
        // `config.account` is specified as the beneficiary address, which will receive any refunds or fees from gas payments.
        // This call initiates the processing of the UserOperation(s) through the Account Abstraction flow.
        IEntryPoint(helperConfig.getConfig().entryPoint).handleOps(ops, payable(helperConfig.getConfig().account));
        vm.stopBroadcast();
    }

    function generateSignedUserOperation(
        bytes memory callData,
        HelperConfig.NetworkConfig memory config,
        address minimalAccount
    ) public view returns (PackedUserOperation memory) {
        // 1. Generate the unsigned data
        uint256 nonce = vm.getNonce(minimalAccount) - 1;
        PackedUserOperation memory userOp = _generateUnsignedUserOperation(callData, minimalAccount, nonce);

        // 2. Get the userOp Hash
        bytes32 userOpHash = IEntryPoint(config.entryPoint).getUserOpHash(userOp);
        bytes32 digest = userOpHash.toEthSignedMessageHash();

        // 3. Sign it
        uint8 v;
        bytes32 r;
        bytes32 s;
        uint256 ANVIL_DEFAULT_KEY = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80;
        if (block.chainid == 31337) {
            (v, r, s) = vm.sign(ANVIL_DEFAULT_KEY, digest);
        } else {
            (v, r, s) = vm.sign(config.account, digest);
        }
        userOp.signature = abi.encodePacked(r, s, v); // Note the order
        return userOp;
    }

    function _generateUnsignedUserOperation(bytes memory callData, address sender, uint256 nonce)
        internal
        pure
        returns (PackedUserOperation memory)
    {
        uint128 verificationGasLimit = 16777216;
        uint128 callGasLimit = verificationGasLimit;
        uint128 maxPriorityFeePerGas = 256;
        uint128 maxFeePerGas = maxPriorityFeePerGas;
        return PackedUserOperation({
            sender: sender,
            nonce: nonce,
            initCode: hex"",
            callData: callData,
            accountGasLimits: bytes32(uint256(verificationGasLimit) << 128 | callGasLimit),
            preVerificationGas: verificationGasLimit,
            gasFees: bytes32(uint256(maxPriorityFeePerGas) << 128 | maxFeePerGas),
            paymasterAndData: hex"",
            signature: hex""
        });
    }
}
