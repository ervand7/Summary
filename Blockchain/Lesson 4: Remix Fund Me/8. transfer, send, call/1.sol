// Get funds from users
// Withdraw funds
// Set a minimum funding value in USD

//  SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;

import "./PriceConverter.sol";

contract FundMe {
    using PriceConverter for uint256;

    uint256 public minimumUSD = 1 * 1e18;

    address[] public funders;
    mapping(address => uint256) public addressToAmountFunded;

    function fund() public payable{
        require(msg.value.getConversionRate() >= minimumUSD, "Didn't send enougth"); // 1e18 == 1 * 10 ** 18 == 1000000000000000000
        funders.push(msg.sender);
        addressToAmountFunded[msg.sender] += msg.value;
    }

    function withdraw() public {
        for (uint256 funderIndex = 0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }

        // reset the array
        funders = new address[](0);

        // https://solidity-by-example.org/sending-ether/
        // transfer. Automatically reverts if the transaction fails:
        // msg.sender = address
        // payable(msg.sender) = payable address
        payable(msg.sender).transfer(address(this).balance);

        // send. Will revert only if we add `require` instruction.
        bool sendSuccess = payable(msg.sender).send(address(this).balance);
        require(sendSuccess, "Send failed");

        // call. For advance usage. Most flexible, forwards all gas, handles complex interactions, requires explicit error handling.
        (bool callSuccess, ) = payable(msg.sender).call{value: address(this).balance}("");
        require(callSuccess, "Call failed");
    }
}