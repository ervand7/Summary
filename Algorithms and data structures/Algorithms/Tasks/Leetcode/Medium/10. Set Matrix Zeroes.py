from typing import List


# my solution
def set_zeroes(matrix: List[List[int]]) -> None:
    indexes_to_be_zero = set()
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        row_contains_zero = False
        for j in range(n):
            if matrix[i][j] == 0:
                row_contains_zero = True
                indexes_to_be_zero.add(j)
        if row_contains_zero:
            for j in range(n):
                matrix[i][j] = 0

    for j in indexes_to_be_zero:
        for row in range(m):
            matrix[row][j] = 0
