from typing import List


def max_increase_keeping_skyline(grid: List[List[int]]) -> int:
    n = len(grid)
    max_rows = [max(row) for row in grid]
    max_columns = []
    for i in range(n):
        max_column = max([row[i] for row in grid])
        max_columns.append(max_column)

    result = 0
    for i in range(n):
        for j in range(n):
            result += min(max_rows[i], max_columns[j]) - grid[i][j]

    return result


print(max_increase_keeping_skyline(grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
