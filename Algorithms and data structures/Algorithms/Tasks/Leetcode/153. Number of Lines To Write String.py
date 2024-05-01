from typing import List

letters = "abcdefghijklmnopqrstuvwxyz"
limit = 100


# my solution
def number_of_lines(widths: List[int], s: str) -> List[int]:
    h = {letters[i]: widths[i] for i in range(len(widths))}
    rows = 1
    last_row_len = 0

    for i in s:
        val = h[i]
        if (last_row_len + val) > limit:
            rows += 1
            last_row_len = val
        else:
            last_row_len += val

    return [rows, last_row_len]
