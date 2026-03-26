from typing import List


# my solution
# Time is O(n²) because we process all elements once across layers;
# Space is O(n) due to temporary arrays per layer.
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # 1) find 4 lists for 4 side walls
    # 2) make new assignment via rotation
    # make the same 2 steps for inner step

    # each step reduces the wall size by 2. Thus, we should stop our cycle if
    # the wall size is < 2

    n = wall_size = len(matrix)
    depth = 0
    start = 0
    end = len(matrix)
    while wall_size >= 2:
        # find the walls
        up = matrix[depth][start:end]
        right = [i[n - 1 - depth] for i in matrix[start:end]]
        down = matrix[n - 1 - depth][start:end]
        left = [i[depth] for i in matrix[start:end]]

        # make rotation
        # up => left
        matrix[depth][start:end] = left[::-1]
        # right => up
        for up_idx, i in enumerate(matrix[start:end]):
            i[n - 1 - depth] = up[up_idx]
        # down => right
        matrix[n - 1 - depth][start:end] = right[::-1]
        # left => down
        for down_idx, i in enumerate(matrix[start:end]):
            i[depth] = down[down_idx]

        wall_size -= 2
        depth += 1
        start += 1
        end -= 1


# ChatGPT solution
# Time is O(n²) since we visit all elements.
# Space is O(1) because rotation is done in-place without extra memory.
def rotate(matrix):
    n = len(matrix)

    # 1. Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reverse each row
    for row in matrix:
        row.reverse()


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
for row in matrix:
    print(row)

print()

rotate(matrix)
for row in matrix:
    print(row)
