from typing import List


# Time: O(m * n)
# Space: O(1)
def minimum_area(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    up = m - 1
    right = 0
    down = 0
    left = n - 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                up = min(up, i)
                right = max(right, j)
                down = max(down, i)
                left = min(left, j)

    return (down + 1 - up) * (right + 1 - left)


print(minimum_area([[0, 1, 0], [1, 0, 1]]))
