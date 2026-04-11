from typing import List


def max_equal_rows_after_flips(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    result = 0

    for j in range(n):
        # flip the column
        for i in range(m):
            matrix[i][j] = 1 if matrix[i][j] == 0 else 1

        attempt = 0
        for row in matrix:
            if len(set(row)) == 1:
                attempt += 1

        result = max(result, attempt)

    return result


print(max_equal_rows_after_flips([[0, 1], [1, 1]]))
