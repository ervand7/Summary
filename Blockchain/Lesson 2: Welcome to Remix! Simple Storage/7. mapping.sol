// SPDX-License-Identifier: MIT

pragma solidity ^0.8.8;

contract  SimpleStorage {
    mapping(string => uint256) public nameToFavoriteNumber;

    function addPerson(uint256 _favoriteNumber, string memory _name) public {
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}

