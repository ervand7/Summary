from typing import List


def ones_minus_zeros(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    result = [[0] * n for _ in range(m)]

    ones_col = []
    zeros_col = []
    for j in range(n):
        ones_col.append([grid[i][j] for i in range(m)].count(1))
        zeros_col.append([grid[i][j] for i in range(m)].count(0))

    for i in range(m):
        ones_row = grid[i].count(1)
        zeros_row = grid[i].count(0)
        for j in range(n):
            result[i][j] = ones_row + ones_col[j] - zeros_row - zeros_col[j]

    return result


# ChatGPT solution
def ones_minus_zeros(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])

    ones_row = [0] * m
    ones_col = [0] * n

    # Count ones in rows and columns
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ones_row[i] += 1
                ones_col[j] += 1

    # Build result
    diff = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            diff[i][j] = 2 * ones_row[i] + 2 * ones_col[j] - m - n

    return diff


print(ones_minus_zeros(grid=[[1, 1, 1], [1, 1, 1]]))
