from typing import List


def find_matrix(nums: List[int]) -> List[List[int]]:
    h = {}
    for i in nums:
        h[i] = h.get(i, 0) + 1

    result = []
    while any(h.values()):
        sublist = []
        for k, v in h.items():
            if v > 0:
                sublist.append(k)
                h[k] -= 1

        result.append(sublist)

    return result
