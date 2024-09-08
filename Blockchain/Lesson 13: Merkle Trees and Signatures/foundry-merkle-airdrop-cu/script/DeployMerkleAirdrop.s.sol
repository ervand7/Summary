// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import { MerkleAirdrop, IERC20 } from "../src/MerkleAirdrop.sol";
import { Script } from "forge-std/Script.sol";
import { BagelToken } from "../src/BagelToken.sol";
import { console } from "forge-std/console.sol";

contract DeployMerkleAirdrop is Script {
    bytes32 public ROOT = 0xaa5d581231e596618465a56aa0f5870ba6e20785fe436d5bfb82b08662ccc7c4;
    // 4 users, 25 Bagel tokens each
    uint256 public AMOUNT_TO_TRANSFER = 4 * (25 * 1e18);

    // Deploy the airdrop contract and bagel token contract
    function deployMerkleAirdrop() public returns (MerkleAirdrop, BagelToken) {
        // Start broadcasting transactions to the blockchain. This allows the function to send state-changing
        // transactions.
        vm.startBroadcast();

        // Deploy a new instance of the BagelToken contract. This creates the token contract with the specified name and
        // symbol.
        BagelToken bagelToken = new BagelToken();

        // Deploy a new instance of the MerkleAirdrop contract.
        // It is initialized with the Merkle root (`ROOT`) and the address of the BagelToken contract.
        // The MerkleAirdrop contract will handle the token distribution to users based on the Merkle root.
        MerkleAirdrop airdrop = new MerkleAirdrop(ROOT, IERC20(bagelToken));

        // Mint the total amount of tokens to the contract owner (usually the deployer of the BagelToken contract).
        // `AMOUNT_TO_TRANSFER` represents the total tokens that will be distributed via the airdrop.
        // This step ensures that the contract owner has enough tokens to transfer to the airdrop contract.
        bagelToken.mint(bagelToken.owner(), AMOUNT_TO_TRANSFER);

        // Transfer the minted tokens from the BagelToken contract to the MerkleAirdrop contract.
        // The `transfer` function sends the total amount of tokens (`AMOUNT_TO_TRANSFER`) to the airdrop contract,
        // which will later distribute these tokens to users who can prove their eligibility via Merkle proofs.
        IERC20(bagelToken).transfer(address(airdrop), AMOUNT_TO_TRANSFER);

        // Stop broadcasting transactions. This ensures that no further state-changing transactions are broadcasted
        // during this execution, which helps control transaction management.
        vm.stopBroadcast();

        // Return the deployed instances of the MerkleAirdrop and BagelToken contracts so they can be used later.
        return (airdrop, bagelToken);
    }

    function run() external returns (MerkleAirdrop, BagelToken) {
        return deployMerkleAirdrop();
    }
}
