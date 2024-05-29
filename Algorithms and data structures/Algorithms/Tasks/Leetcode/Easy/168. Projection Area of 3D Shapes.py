from typing import List


# у задачи абсолютно ужасное описания. Я так и не понял условия
def projection_area(grid: List[List[int]]) -> int:
    xy_projection = sum(val > 0 for row in grid for val in row)
    yz_projection = sum(max(col) for col in zip(*grid))
    zx_projection = sum(max(row) for row in grid)

    return xy_projection + yz_projection + zx_projection
