// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/*
 * @title OracleLib
 * @author Ervand Agadzhanyan
 * @notice This library is used to check the Chainlink Oracle for stale data.
 * If a price is stale, functions will revert, and render the DSCEngine unusable - this is by design.
 * We want the DSCEngine to freeze if prices become stale.
 *
 * So if the Chainlink network explodes and you have a lot of money locked in the protocol... too bad.
 */
library OracleLib {
    error OracleLib__StalePrice();

    uint256 private constant TIMEOUT = 3 hours;

    function staleCheckLatestRoundData(AggregatorV3Interface chainlinkFeed)
        public
        view
        returns (uint80, int256, uint256, uint256, uint80)
    {
        // Retrieve the latest round data from the Chainlink oracle.
        // Example: Assume the latest price of ETH/USD is $2000, and the data was last updated 1 hour ago.
        (uint80 roundId, int256 answer, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound) =
            chainlinkFeed.latestRoundData();

        // Check if the price data is invalid by verifying if 'updatedAt' is zero.
        // Example: If 'updatedAt' is 0, it means no price data is available, so we cannot rely on it.
        // Also check if 'answeredInRound' is less than 'roundId', which suggests the data is not from the latest round.
        // Example: If roundId is 10 and answeredInRound is 9, it indicates the data might be stale.
        if (updatedAt == 0 || answeredInRound < roundId) {
            // Revert the transaction with a custom error if the data is invalid.
            // Example: If either condition is true, the function will stop execution and return an error.
            revert OracleLib__StalePrice();
        }

        // Calculate the number of seconds that have passed since the last price update.
        // Example: Assume the current block.timestamp is 1650000000 and 'updatedAt' is 1649996400 (1 hour ago).
        // This would result in 'secondsSince' being 3600 seconds.
        uint256 secondsSince = block.timestamp - updatedAt;

        // If the time elapsed since the last update exceeds the TIMEOUT threshold, revert the transaction.
        // Example: The TIMEOUT is 3 hours (10800 seconds). If 'secondsSince' is greater than 10800, it means the data is too old.
        if (secondsSince > TIMEOUT) revert OracleLib__StalePrice();

        // Return the latest round data if all checks pass and the data is valid.
        // Example: If all conditions are met, the function will return the current roundId, price ($2000),
        // and the other relevant timestamps, confirming that the data is fresh and can be used.
        return (roundId, answer, startedAt, updatedAt, answeredInRound);
    }

    function getTimeout(AggregatorV3Interface /* chainlinkFeed */ ) public pure returns (uint256) {
        return TIMEOUT;
    }
}
