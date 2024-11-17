from typing import List


def generate_matrix(n: int) -> List[List[int]]:
    if n == 1:
        return [[1]]

    counter = 1
    result = [[0] * n for _ in range(n)]

    def rec(level: int):
        nonlocal counter

        if counter > n * n:
            return

        # fill the first row
        for i in range(level, n - level):
            result[level][i] = counter
            counter += 1
            if counter > n * n:
                return

        # fill right side
        for i in range(level + 1, n - 1 - level):
            result[i][-1 - level] = counter
            counter += 1

        # fill the last row
        for i in range(n - 1 - level, level - 1, -1):
            result[n - 1 - level][i] = counter
            counter += 1

        # fill left side
        for i in range(n - 2 - level, level, -1):
            result[i][level] = counter
            counter += 1

        rec(level=level + 1)

    rec(level=0)
    return result


generate_matrix(10)
