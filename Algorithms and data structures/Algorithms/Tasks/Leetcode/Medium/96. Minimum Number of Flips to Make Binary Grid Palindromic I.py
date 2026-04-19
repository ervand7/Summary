from typing import List


# Time: O(m * n)
# Space: O(1)
# my solution
def min_flips(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    row_mid = n // 2
    column_mid = m // 2
    row_steps = 0
    column_steps = 0

    # count by rows
    for i in range(m):
        for j in range(row_mid):
            if grid[i][j] != grid[i][n - 1 - j]:
                row_steps += 1

    # count by columns
    for j in range(n):
        for i in range(column_mid):
            if grid[i][j] != grid[m - 1 - i][j]:
                column_steps += 1

    return min(row_steps, column_steps)


# ChatGPT solution
def min_flips(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    row_flips = 0
    for i in range(m):
        l, r = 0, n - 1
        while l < r:
            if grid[i][l] != grid[i][r]:
                row_flips += 1
            l += 1
            r -= 1

    col_flips = 0
    for j in range(n):
        top, bottom = 0, m - 1
        while top < bottom:
            if grid[top][j] != grid[bottom][j]:
                col_flips += 1
            top += 1
            bottom -= 1

    return min(row_flips, col_flips)
