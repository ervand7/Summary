# ChatGPT solution
from typing import List


def all_cells_dist_order(rows: int, cols: int, r_center: int, c_center: int) -> List[List[int]]:
    cells = []
    for r in range(rows):
        for c in range(cols):
            cells.append((r, c))

    cells.sort(key=lambda cell: abs(cell[0] - r_center) + abs(cell[1] - c_center))

    return cells
