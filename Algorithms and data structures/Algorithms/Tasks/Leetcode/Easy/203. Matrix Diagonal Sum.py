from typing import List


# my solution
def diagonal_sum(mat: List[List[int]]) -> int:
    n = len(mat)
    total = 0

    for i in range(n):
        total += mat[i][i]
        total += mat[i][n - 1 - i]

    if n % 2 == 1:
        total -= mat[n // 2][n // 2]

    return total
