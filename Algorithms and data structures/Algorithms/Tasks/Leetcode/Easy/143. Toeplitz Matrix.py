from typing import List


def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    m, n = len(matrix), len(matrix[0])
    for i in range(m - 1):  # Exclude the last row
        for j in range(n - 1):  # Exclude the last column
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False

    return True
