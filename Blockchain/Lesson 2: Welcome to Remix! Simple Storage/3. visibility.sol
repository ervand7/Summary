// SPDX-License-Identifier: MIT

// function visibility specifier:
// https://docs.soliditylang.org/en/latest/contracts.html#visibility-and-getters

pragma solidity 0.8.8;

contract  SimpleStorage {
    // internal is default visibility specifier
    uint public favoriteNumber; // will be set the default val

    function store(uint256 num) public {
        favoriteNumber = num;
    }
}

