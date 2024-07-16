// SPDX-License-Identifier: MIT

pragma solidity ^0.8.8;

contract  SimpleStorage {
    // favoriteNumber automatically will be store in storage
    uint256 favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }
    People public person = People({favoriteNumber: 2, name: "Patrick"});
    People[] public peoples;

    // calldata, memory, stotage
    function addPerson(uint256 _favoriteNumber, string memory _name) public {
        peoples.push(People(_favoriteNumber, _name));
    }
}

