from typing import List


# my solution
# Time: O(m · n²)
# Space: O(m · n)
def rotate_the_box(box_grid: List[List[str]]) -> List[List[str]]:
    # 1) define variables
    stone = "#"
    obstacle = "*"
    empty = "."

    n = len(box_grid[0])

    # 2) process each row as it is, horizontally
    # 2.1 find the nearest obstacle and try to fill all empty cells by in-pace algorithm
    def find_nearest_obstacle_idx(row: List[int], start: int) -> int:
        for i in range(start, n):
            if row[i] == obstacle:
                return i
        return n

    for row in box_grid:
        start = 0
        while start < n:
            end = find_nearest_obstacle_idx(row, start)
            count_empty = row[start:end].count(empty)
            count_stone = row[start:end].count(stone)
            moved = [empty] * count_empty + [stone] * count_stone
            row[start:end] = moved
            start = end + 1

    # 3) simulate 90 degrees rotation
    result = []
    for col in range(n):
        row = [i[col] for i in box_grid][::-1]
        result.append(row)

    return result


# ChatGPT solution
# Time: O(m * n)
# Space: O(m * n)
def rotate_the_box(box_grid: List[List[str]]) -> List[List[str]]:
    m, n = len(box_grid), len(box_grid[0])

    # Step 1: simulate gravity in each row
    # Stones fall to the right before rotation
    for i in range(m):
        write = n - 1  # next place where a stone can land

        for j in range(n - 1, -1, -1):
            if box_grid[i][j] == '*':
                write = j - 1
            elif box_grid[i][j] == '#':
                box_grid[i][j] = '.'
                box_grid[i][write] = '#'
                write -= 1

    # Step 2: rotate 90 degrees clockwise
    result = [[''] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m - 1 - i] = box_grid[i][j]

    return result


print(rotate_the_box(
    [["#", "#", "*", ".", "*", "."],
     ["#", "#", "#", "*", ".", "."],
     ["#", "#", "#", ".", "#", "."]])
)
