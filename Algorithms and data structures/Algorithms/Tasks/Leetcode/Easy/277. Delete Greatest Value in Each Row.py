from typing import List


def delete_greatest_value(grid: List[List[int]]) -> int:
    result = 0
    for i in range(len(grid)):
        grid[i].sort()
    while any(grid):
        max_val = -float("inf")
        for i in range(len(grid)):
            max_per_row = grid[i].pop()
            max_val = max(max_val, max_per_row)

        result += max_val

    return result
