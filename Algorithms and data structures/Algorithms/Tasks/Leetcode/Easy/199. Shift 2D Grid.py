from typing import List


def shift_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    unpacked = []
    for i in grid:
        unpacked.extend(i)

    k = k % len(unpacked)

    rearranged = unpacked[-k:] + unpacked[:-k]
    result = []
    cell = []
    limit = len(grid[0])

    for i in rearranged:
        cell.append(i)
        if len(cell) == limit:
            result.append(cell)
            cell = []

    return result
