// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import { ERC20 } from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import { Ownable } from "@openzeppelin/contracts/access/Ownable.sol";

// This is token for MercleAirdrop contract
contract BagelToken is ERC20, Ownable {
    // In Solidity, Ownable is a contract from OpenZeppelin that defines a simple 
    // ownership model. When you call Ownable(msg.sender) in the constructor, you're 
    // setting the msg.sender (the address that deployed the contract) as the initial 
    // owner of the contract. This is important because certain functions, like the 
    // mint function in your contract, are restricted to the owner only, ensuring 
    // that only the contract owner can perform these actions.
    constructor() ERC20("Bagel Token", "BT") Ownable(msg.sender) { 
    }

    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }
}
