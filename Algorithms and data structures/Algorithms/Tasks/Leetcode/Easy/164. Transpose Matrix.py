from typing import List


# my solution
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return list(zip(*matrix))


# my solution
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    result = []
    for j in range(len(matrix[0])):
        result.append([matrix[i][j] for i in range(len(matrix))])

    return result


# ChatGPT solution
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    transposed = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            transposed[j][i] = matrix[i][j]

    return transposed


print(transpose(matrix=[[1, 2, 3, 4], [4, 5, 6, 7]]))
