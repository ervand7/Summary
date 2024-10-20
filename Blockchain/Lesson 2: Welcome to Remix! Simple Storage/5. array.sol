// SPDX-License-Identifier: MIT

pragma solidity ^0.8.8;

contract  SimpleStorage {
    uint256 favoriteNumber;
    function store(uint256 num) public {
        favoriteNumber = num;
    }

    struct People {
        uint256 favoriteNumber;
        string name;
    }
    People public person = People({favoriteNumber: 2, name: "Patrick"});
    People[] public peoples;

    function addPerson(uint256 _favoriteNumber, string memory _name) public {
        peoples.push(People(_favoriteNumber, _name));
    }
}

