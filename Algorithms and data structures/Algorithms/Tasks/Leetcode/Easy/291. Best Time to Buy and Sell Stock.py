from typing import List


# my slow solution
def maxProfit(prices: List[int]) -> int:
    result = 0
    n = len(prices)
    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = prices[i] - prices[j]
            result = max(result, -diff)

    return result


def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
