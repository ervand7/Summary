from typing import List


# my solution
def number_of_alternating_groups(colors: List[int]) -> int:
    n = len(colors)
    result = 0
    for i in range(n):
        a, b, c = colors[i % n], colors[(i + 1) % n], colors[(i + 2) % n]
        if a == c and a != b:
            result += 1

    return result
