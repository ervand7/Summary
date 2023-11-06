from typing import List


# my solution
def searchInsert(nums: List[int], target: int) -> int:
    if nums[-1] < target:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] >= target:
            return i


print(searchInsert(nums=[1, 3, 5, 6], target=7))
