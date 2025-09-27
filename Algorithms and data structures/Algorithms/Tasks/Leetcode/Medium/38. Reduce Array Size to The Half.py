from typing import List


# my solution
def min_set_size(arr: List[int]) -> int:
    h = {}
    for i in arr:
        h[i] = h.get(i, 0) + 1

    h_sorted = sorted(h.values(), reverse=True)
    half = len(arr) // 2
    result = 0
    val = 0
    for i in h_sorted:
        result += 1
        val += i
        if val >= half:
            break

    return result
