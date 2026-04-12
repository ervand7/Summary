from typing import List


# my solution
# Time: O(m² · n)
# Space: O(n)
def max_equal_rows_after_flips(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    result = 0

    for num in [0, 1]:
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != num:
                    # flip
                    for row in range(m):
                        matrix[row][j] = 1 if matrix[row][j] == 0 else 0

            attempt = 0
            for row in matrix:
                if len(set(row)) == 1:
                    attempt += 1

                result = max(result, attempt)

    return result


from collections import Counter

# ChatGPT solution
# Time: O(m * n)
# Space: O(m * n)
def max_equal_rows_after_flips(matrix: List[List[int]]) -> int:
    count = Counter()

    for row in matrix:
        if row[0] == 0:
            pattern = tuple(row)
        else:
            pattern = tuple(1 - x for x in row)

        count[pattern] += 1

    return max(count.values())


print(max_equal_rows_after_flips(
    [
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    ]))
