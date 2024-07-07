// SPDX-License-Identifier: MIT

pragma solidity 0.8.8;

contract  SimpleStorage {
    uint favoriteNumber; // will be set the default val

    function store(uint256 num) public {
        favoriteNumber = num;
    }
}

// 0xd9145CCE52D386f254917e481eB44e9943F39138 - this is address of out smart contract