from typing import List


# my solution
def third_max(nums: List[int]) -> int:
    lst = sorted(set(nums), reverse=True)
    return lst[2] if len(lst) >= 3 else lst[0]
