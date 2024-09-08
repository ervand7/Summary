// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import { Script, console } from "forge-std/Script.sol";
import { DevOpsTools } from "foundry-devops/src/DevOpsTools.sol";
import { MerkleAirdrop } from "../src/MerkleAirdrop.sol";

contract ClaimAirdrop is Script {
    address private constant CLAIMING_ADDRESS = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
    uint256 private constant AMOUNT_TO_COLLECT = (25 * 1e18);

    bytes32 private constant PROOF_ONE = 0xd1445c931158119b00449ffcac3c947d028c0c359c34a6646d95962b3b55c6ad;
    bytes32 private constant PROOF_TWO = 0xe5ebd1e1b5a5478a944ecab36a9a954ac3b6b8216875f6524caa7a1d87096576;
    bytes32[] private proof = [PROOF_ONE, PROOF_TWO];

    // the signature will change every time you redeploy the airdrop contract!
    // see https://github.com/Cyfrin/foundry-merkle-airdrop-cu/blob/main/README.md#sign-your-airdrop-claim
    bytes private SIGNATURE =
        hex"04209f8dfd0ef06724e83d623207ba8c33b6690e08772f8887a4eaf9a66b9182188938adea374fa542ad5ddde24bdc981f5e26a628e65fb425a68db8a938f6761c";

    error __ClaimAirdropScript__InvalidSignatureLength();

    function run() external {
        address mostRecentlyDeployed = DevOpsTools.get_most_recent_deployment("MerkleAirdrop", block.chainid);
        claimAirdrop(mostRecentlyDeployed);
    }

    function claimAirdrop(address airdrop) public {
        vm.startBroadcast();

        // Split the provided ECDSA signature into its three components: v (recovery id), r, and s.
        // This is necessary because Solidity's `ecrecover` function (used in signature validation) 
        // requires these three components.
        (uint8 v, bytes32 r, bytes32 s) = splitSignature(SIGNATURE);
        console.log("Claiming Airdrop");

        // Call the `claim` function on the MerkleAirdrop contract.
        // The `claim` function is invoked with the following arguments:
        // - CLAIMING_ADDRESS: the address of the account claiming the tokens.
        // - AMOUNT_TO_COLLECT: the amount of tokens being claimed.
        // - proof: a Merkle proof, represented by an array of hashes (this proves that the claimant is eligible).
        // - v, r, s: the signature components that will be used to verify the signature and ensure it is valid.
        MerkleAirdrop(airdrop).claim(CLAIMING_ADDRESS, AMOUNT_TO_COLLECT, proof, v, r, s);
        vm.stopBroadcast();
        console.log("Claimed Airdrop");
    }

    function splitSignature(bytes memory sig) public pure returns (uint8 v, bytes32 r, bytes32 s) {
        // Check if the provided signature has the correct length (65 bytes).
        // ECDSA signatures are always 65 bytes: 32 bytes for `r`, 32 bytes for `s`, and 1 byte for `v`.
        if (sig.length != 65) {
            // Revert the transaction if the signature length is not exactly 65 bytes and throw a custom error.
            revert __ClaimAirdropScript__InvalidSignatureLength();
        }

        // Use assembly to manually extract the `r`, `s`, and `v` values from the signature.
        // Assembly allows direct access to memory, which is used here to pull out the relevant components.
        assembly {
            // The first 32 bytes of the signature (after the first 32-byte word) are loaded into `r`.
            r := mload(add(sig, 32))
            // The second 32 bytes (next word in memory) are loaded into `s`.
            s := mload(add(sig, 64))
            // The last byte (offset by 96 bytes) is loaded into `v` (this is the recovery id).
            v := byte(0, mload(add(sig, 96)))
        }
    }
}
