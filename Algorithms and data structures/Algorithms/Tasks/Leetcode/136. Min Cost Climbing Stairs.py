from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    n = len(cost)
    prev, curr = 0, 0
    for i in range(2, n + 1):
        next = min(curr + cost[i - 1], prev + cost[i - 2])
        prev, curr = curr, next

    return curr


print(min_cost_climbing_stairs([10, 15, 25]))
