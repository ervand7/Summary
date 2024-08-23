// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/*
This is an example of not manual token creation, using @openzeppelin/contracts/token/ERC20/ERC20.sol
*/

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract OurToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("OurToken", "OT") {
        _mint(msg.sender, initialSupply);
    }
}
