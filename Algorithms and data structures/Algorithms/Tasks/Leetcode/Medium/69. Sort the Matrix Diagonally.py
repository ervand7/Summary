from typing import List
from pprint import pprint


def diagonal_sort(mat: List[List[int]]) -> List[List[int]]:
    # we should make 2 traverses:
    # - main
    # - for remains

    # main traverse
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        m_range = (min(m, n - i))
        diagonal_values = [mat[j + i][j] for j in range(m_range)]
        diagonal_values.sort()

        for j in range(m_range):
            mat[j + i][j] = diagonal_values[j]

    # traverse for remained values
    for i in range(1, m):
        m_range = min(n, m - i)
        diagonal_values = [mat[j][j + i] for j in range(m_range)]
        diagonal_values.sort()

        for j in range(m_range):
            mat[j][j + i] = diagonal_values[j]

    return mat


arr = [
    [5, 2, 5, 6, 9, 3, 4],
    [7, 2, 5, 6, 9, 3, 4],
    [5, 2, 0, 6, 9, 3, 4],
    [2, 2, 5, 3, 9, 3, 4],
    [7, 1, 3, 1, 1, 3, 4]
]

diagonal_sort(arr)

pprint(arr)
