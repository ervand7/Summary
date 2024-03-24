from typing import List


# my solution
def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    data = []
    for i in mat:
        data += i

    if r * c > len(data):
        return mat

    result = []
    check_count = 0
    step = len(data) // r
    start = 0
    end = step
    for _ in range(r):
        element = data[start:end]
        check_count += len(element)
        result.append(element)
        start += step
        end += step

    if len(data) != check_count:
        return mat
    return result


# ChatGPT solution
def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat

    reshaped = [[0 for _ in range(c)] for _ in range(r)]
    count = 0

    for i in range(m):
        for j in range(n):
            reshaped[count // c][count % c] = mat[i][j]
            count += 1

    return reshaped


print(matrix_reshape([[1, 2], [3, 4]], 1, 4))
