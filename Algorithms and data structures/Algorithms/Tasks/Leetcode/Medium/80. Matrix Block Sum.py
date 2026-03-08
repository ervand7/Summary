from typing import List


def matrix_block_sum(mat: List[List[int]], k: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    result = [[0] * n for _ in range(m)]

    # iter on each mat[r][c]
    # find all borders around cell in radius k
    # calc them sum and paste to result

    for i in range(m):
        for j in range(n):
            up = max(i - k, 0)
            right = min(j + k, n - 1)
            down = min(i + k, m - 1)
            left = max(j - k, 0)

            summa = 0
            for row in range(up, down + 1):
                summa += sum(mat[row][left:right + 1])
            result[i][j] = summa

    return result
