// Get funds from users
// Withdraw funds
// Set a minimum funding value in USD

//  SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    uint256 public minimumUSD = 1 * 1e18;

    function fund() public payable{
        require(getConversionRate(msg.value) >= minimumUSD, "Didn't send enougth"); // 1e18 == 1 * 10 ** 18 == 1000000000000000000
    }

    function getPrice() public view returns (uint256){
        // ABI
        // Address 0x694AA1769357215DE4FAC081bf1f309aDC325306 (from https://docs.chain.link/data-feeds/price-feeds/addresses/?network=ethereum&page=1#sepolia-testnet )
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        (, int price,,,) = priceFeed.latestRoundData();
        // ETH in terms of USD
        // 3000.00000000

        return uint256(price * 1e10); // 1**10 == 10000000000
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        return priceFeed.version();
    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        // 3000_000000000000000000 = ETH / USD price
        // 1_000000000000000000 ETH
        uint256 ethAmountInUsd = (ethPrice *  ethAmount) / 1e18;

        // 3000
        return ethAmountInUsd;
    }

}