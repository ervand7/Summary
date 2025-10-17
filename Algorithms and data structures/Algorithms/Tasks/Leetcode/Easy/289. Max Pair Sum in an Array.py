from typing import List


def max_sum(nums: List[int]) -> int:
    h = {}
    for i in nums:
        max_val = max([int(v) for v in str(i)])
        if h.get(max_val):
            h[max_val].append(i)
        else:
            h[max_val] = [i]

    result = -1
    for _, v in h.items():
        if len(v) >= 2:
            t = sum(sorted(v, reverse=True)[:2])
            result = max(result, t)

    return result
