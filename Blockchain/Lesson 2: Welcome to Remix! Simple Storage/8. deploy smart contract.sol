// SPDX-License-Identifier: MIT

// Use "Injected Provider - MetaMask"
// Maybe you will need https://docs.chain.link/resources/link-token-contracts#sepolia-testnet

pragma solidity ^0.8.8;

contract  SimpleStorage {
    uint256 favoriteNumber;
    function store(uint256 num) public {
        favoriteNumber = num;
    }

    mapping(string => uint256) public nameToFavoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }
    People public person = People({favoriteNumber: 2, name: "Patrick"});
    People[] public peoples;

    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }

    function addPerson(uint256 _favoriteNumber, string memory _name) public {
        peoples.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}

