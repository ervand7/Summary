from typing import List


def max_profit(prices: List[int]) -> int:
    if len(prices) == 0:
        return 0

    last = prices[-1]
    profit = 0

    for i in prices[::-1]:
        if last - i > profit:
            profit = last - i
        if i > last:
            last = i

    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))
