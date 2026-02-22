from typing import List


def restore_matrix(row_sum: List[int], col_sum: List[int]) -> List[List[int]]:
    m = len(row_sum)
    n = len(col_sum)
    matrix = [[i] + [0] * (n - 1) for i in row_sum]

    for j_idx, j in enumerate(col_sum):
        credit = j
        for i in range(m):
            tmp = credit - matrix[i][j_idx]
            if tmp >= 0:
                credit = tmp
            else:
                right_val = matrix[i][j_idx] - credit
                matrix[i][j_idx] = credit
                matrix[i][j_idx + 1] = right_val
                credit -= matrix[i][j_idx]

    return matrix


# ChatGPT solution
def restore_matrix(row_sum: List[int], col_sum: List[int]) -> List[List[int]]:
    m, n = len(row_sum), len(col_sum)
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            val = min(row_sum[i], col_sum[j])
            matrix[i][j] = val
            row_sum[i] -= val
            col_sum[j] -= val

    return matrix


print(restore_matrix(row_sum=[5, 7, 10], col_sum=[8, 6, 8]))
