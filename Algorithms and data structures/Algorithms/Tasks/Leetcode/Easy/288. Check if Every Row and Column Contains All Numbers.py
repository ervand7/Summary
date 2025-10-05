from typing import List


def check_valid(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    match = set(range(1, n + 1))
    for idx in range(0, n):
        if match != set(i[idx] for i in matrix):
            return False

    return all(set(i) == match for i in matrix)
