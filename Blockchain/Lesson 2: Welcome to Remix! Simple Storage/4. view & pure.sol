// SPDX-License-Identifier: MIT

pragma solidity 0.8.8;

contract  SimpleStorage {
    uint public favoriteNumber;

    function store(uint256 num) public {
        favoriteNumber = num;
    }

    // view:
    // Функции могут читать данные из блокчейна, но не могут изменять их.
    // Например, они могут читать значения переменных состояния контракта.
    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }

    // pure:
    // Функции не могут ни читать, ни изменять данные блокчейна.
    // Они могут работать только с входными аргументами и локальными переменными.
    function add() public pure returns (uint256){
        return (1 + 1);
    }
}

