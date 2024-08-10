// Get funds from users
// Withdraw funds
// Set a minimum funding value in USD

//  SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    uint256 public minimumUSD = 1 * 1e18;

    function fund() public payable {
        require(getConversionRate(msg.value) >= minimumUSD, "Didn't send enough");
    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        // если отправляем чуть больше 5 долларов (приблизительно 0.002) то (2586985009380000000000 * 0.002) / 1e18 = 5.1739700187599995
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1e18; // (2586985009380000000000 * 0.002) / 1e18

        return ethAmountInUsd;
    }

    function getPrice() public view returns (uint256){
        // Address 0x694AA1769357215DE4FAC081bf1f309aDC325306 (from https://docs.chain.link/data-feeds/price-feeds/addresses/?network=ethereum&page=1#sepolia-testnet )
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        (, int price,,,) = priceFeed.latestRoundData();
        // ETH in terms of USD

        return uint256(price * 1e10); // 258698500938 * 1e10 = 2586985009380000000000
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        return priceFeed.version();
    }
}