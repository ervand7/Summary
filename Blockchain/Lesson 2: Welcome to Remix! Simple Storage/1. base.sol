// SPDX-License-Identifier: MIT

// pragma solidity ^0.8.7 - any version include and above 0.8.7 untill  0.9.0 (not included)
// pragma solidity >=0.8.7 - also available
// pragma solidity >=0.8.7 <0.9.0 - also available

// command+S - compile
pragma solidity 0.8.8;

contract SimpleStorage {
    // boolean, uint, int, address, bytes
    bool hasFavoriteNumber = true; // false
    uint a = 1;
    int b = - 1;
    string c = "qwe";
    address myAddress = 0xc97Ca114c952EA557f49eF605c0F3864c794B373;
    bytes32 d = "cat";
}