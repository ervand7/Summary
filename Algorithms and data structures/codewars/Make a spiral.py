from itertools import cycle


def spiralize(size: int):
    directions: cycle = cycle(
        ((1, 0), (0, 1), (-1, 0), (0, -1))
    )

    spiral = [[0] * size for _ in range(size)]
    x, y = 0, 0
    direction_changes = 0

    while direction_changes < size:
        change_x, change_y = next(directions)

        while y + change_y in range(size) and x + change_x in range(size):
            spiral[y][x] = 1

            step: bool = y + (change_y * 2) in range(size) \
                         and x + (change_x * 2) in range(size)
            index_y: int = y + (change_y * 2)
            index_x: int = x + (change_x * 2)
            res = step and spiral[index_y][index_x] == 1
            if res:
                break

            y += change_y
            x += change_x
        direction_changes += 1

    return spiral
