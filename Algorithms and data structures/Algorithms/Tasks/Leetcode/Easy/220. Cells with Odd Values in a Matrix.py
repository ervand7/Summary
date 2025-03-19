from typing import List


# my solution
def odd_ells(m: int, n: int, indices: List[List[int]]) -> int:
    matrix = [[0] * n for _ in range(m)]

    for r, c in indices:
        matrix[r] = [i + 1 for i in matrix[r]]
        for row in range(len(matrix)):
            matrix[row][c] = matrix[row][c] + 1

    result = 0
    for i in matrix:
        for j in i:
            if j % 2 == 1:
                result += 1

    return result


# ChatGPT solution
def odd_ells(m: int, n: int, indices: List[List[int]]) -> int:
    row_counts = [0] * m
    col_counts = [0] * n

    # Apply increments
    for ri, ci in indices:
        row_counts[ri] += 1
        col_counts[ci] += 1

    # Count odd rows and odd columns
    odd_rows = sum(1 for x in row_counts if x % 2 == 1)
    odd_cols = sum(1 for x in col_counts if x % 2 == 1)

    # Compute odd cells using the formula
    return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols


print(odd_ells(2, 3, [[0, 1], [1, 1]]))
