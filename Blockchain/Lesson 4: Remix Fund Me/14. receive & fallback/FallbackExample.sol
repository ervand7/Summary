// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract FallbackExample {
    uint256 public result;

    // must be declared as external and payable.
    fallback() external payable {
        result = 1;
    }

    // must be declared as external and payable.
    receive() external payable {
        result = 2;
    }
}

    // Explainer from: https://solidity-by-example.org/fallback/
    // Ether is sent to contract
    //      is msg.data empty?
    //          /   \
    //         yes  no
    //         /     \
    //    receive()  fallback()
    //     /   \
    //   yes   no
    //  /        \
    //receive()  fallback()