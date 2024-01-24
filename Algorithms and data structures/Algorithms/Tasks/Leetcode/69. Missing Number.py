from typing import List


# my solution
def missing_number(nums: List[int]) -> int:
    nums = {i: True for i in nums}
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
