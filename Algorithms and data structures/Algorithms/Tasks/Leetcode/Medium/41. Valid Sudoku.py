import time
from typing import List


# my solution
def is_valid_sudoku(board: List[List[str]]) -> bool:
    len_row = len(board[0])

    # check whether each row contains the digits 1-9 without repetition
    for row in board:
        row_digits = [i for i in row if i.isdigit()]
        if len(row_digits) != len(set(row_digits)):
            return False

    # check whether each column contains the digits 1-9 without repetition
    for idx in range(len_row):
        column_digits = [c[idx] for c in board if c[idx].isdigit()]
        if len(column_digits) != len(set(column_digits)):
            return False

    # check whether each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition
    shift = 0
    while shift < len_row:
        a = board[shift]
        b = board[shift + 1]
        c = board[shift + 2]

        start = 0
        end = 3
        while end <= len_row:
            cube = a[start:end] + b[start:end] + c[start:end]
            filtered_cube = [i for i in cube if i.isdigit()]
            if len(filtered_cube) != len(set(filtered_cube)):
                return False

            start = end
            end += 3

        shift += 3

    return True


# ChatGPT solution
def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue

            box_index = (r // 3) * 3 + (c // 3)

            if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                return False

            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],

    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],

    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(is_valid_sudoku(board))
