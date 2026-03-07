from typing import List


def buy_and_sell(data: List[int]) -> int:
    result, temp_max = 0, 0
    for i in reversed(data):
        temp_max = max(temp_max, i)
        profit = temp_max - i
        result = max(profit, result)

    return result


print(buy_and_sell([8, 10, 7, 5, 7, 15]))
