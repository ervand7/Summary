from typing import List


# my solution
def minimum_abs_difference(arr: List[int]) -> List[List[int]]:
    arr.sort()
    minimum = float('inf')
    result = []
    for i in range(1, len(arr)):
        a, b = arr[i - 1], arr[i]
        diff = b - a
        if diff == minimum:
            result.append([a, b])
        elif diff < minimum:
            result = [[a, b]]
            minimum = diff

    return result
