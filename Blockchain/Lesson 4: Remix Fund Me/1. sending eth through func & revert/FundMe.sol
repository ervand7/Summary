//  SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;

contract FundMe {

    // Инструкция payable означает, что функция может принимать и обрабатывать платежи в Ether
    function fund() public payable {
        // msg.value is in Wei
        require(msg.value > 1e18, "Didn't send enougth"); // 1e18 == 1 * 10 ** 18 == 1000000000000000000
    }
}