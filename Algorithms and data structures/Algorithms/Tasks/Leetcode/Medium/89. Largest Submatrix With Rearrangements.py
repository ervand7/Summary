from typing import List


# my solution (fails by time)
def largest_submatrix(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])

    h = {}
    for j in range(n):
        start = None
        add = True
        for i in range(m):
            if matrix[i][j] == 1:
                if add:
                    start = i
                    add = False

                if i == m - 1:
                    end = m
                    for a in range(start, end + 1):
                        for b in range(a + 1, end + 1):
                            diapason = tuple(range(a, b))
                            h[diapason] = h.get(diapason, 0) + 1

            else:
                if start is not None:
                    end = i
                    for a in range(start, end + 1):
                        for b in range(a + 1, end + 1):
                            diapason = tuple(range(a, b))
                            h[diapason] = h.get(diapason, 0) + 1
                start = None
                add = True

    result = 0
    for k, v in h.items():
        result = max(result, len(k) * v)

    return result


# ChatGPT solution
# O(m * (n log n))
def largest_submatrix(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])

    # Step 1: build heights
    heights = [0] * n
    res = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                heights[j] = 0
            else:
                heights[j] += 1

        # Step 2: sort heights descending
        sorted_h = sorted(heights, reverse=True)

        # Step 3: compute max area
        for k in range(n):
            res = max(res, sorted_h[k] * (k + 1))

    return res


print(largest_submatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
