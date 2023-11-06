from typing import List


def maxProfit(prices: List[int]) -> int:
    if len(prices) == 0:
        return 0

    last = prices[-1]
    profit = 0

    for item in prices[::-1]:
        if last - item > profit:
            profit = last - item
        if item > last:
            last = item
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
