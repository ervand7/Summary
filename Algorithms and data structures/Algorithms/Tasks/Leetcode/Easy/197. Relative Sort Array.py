from typing import List


# my solution
def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    arr2_set = set(arr2)
    excluded = []
    h = {}
    for i in arr1:
        if i in arr2_set:
            h[i] = h.get(i, 0) + 1
        else:
            excluded.append(i)

    result = []
    for i in arr2:
        result.extend([i] * h[i])

    return result + sorted(excluded)
