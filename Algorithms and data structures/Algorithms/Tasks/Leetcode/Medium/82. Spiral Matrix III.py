from typing import List


def spiral_matrix_iii(rows: int, cols: int, r_start: int, c_start: int) -> List[List[int]]:
    result = [[r_start, c_start]]
    r, c = r_start, c_start
    step = 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while len(result) < rows * cols:
        for d in range(4):
            dr, dc = directions[d]

            for _ in range(step):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])

            if d % 2 == 1:
                step += 1

    return result


print(spiral_matrix_iii(rows=5, cols=6, r_start=1, c_start=4))
