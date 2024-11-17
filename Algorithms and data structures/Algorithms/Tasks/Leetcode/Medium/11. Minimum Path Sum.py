from typing import List


# ChatGpt solution
def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # Update the first row
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]

    # Update the first column
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]

    # Update the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    # The result is in the bottom-right corner
    return grid[m - 1][n - 1]
