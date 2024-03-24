from typing import List


# ChatGPT solution
def max_count(m: int, n: int, ops: List[List[int]]) -> int:
    if not ops:
        return m * n

    # Find the minimum values of a and b in all operations, as these will determine the size of the submatrix
    # that gets incremented in every operation
    min_a = min(op[0] for op in ops)
    min_b = min(op[1] for op in ops)

    # The count of maximum integers is the area of the smallest submatrix defined by the operations
    return min_a * min_b


print(max_count(m=39999, n=39999, ops=[[19999, 19999]]))


# my solution (works badL: slow in big data)
def max_count(m: int, n: int, ops: List[List[int]]) -> int:
    if not ops:
        return m * n

    result = [[0 for i in range(m)] for j in range(n)]
    for i, j in ops:
        for _i in range(i):
            for _j in range(j):
                result[_i][_j] += 1

    h = {}
    for i in result:
        for j in i:
            h[j] = h.get(j, 0) + 1

    m = max(list(h.keys()))

    return h[m]
