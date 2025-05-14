from typing import List


# my solution
def most_frequent_even(nums: List[int]) -> int:
    h = {}
    for i in nums:
        if i % 2 == 0:
            h[i] = h.get(i, 0) + 1

    if len(h) == 0:
        return -1

    max_val = float("inf")
    counter = 0
    for k, v in h.items():
        if v > counter:
            max_val = k
            counter = v

        elif v == counter:
            if k < max_val:
                max_val = k

    return max_val
