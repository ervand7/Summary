from typing import List


# my solution
def search_insert_idx(nums: List[int], target: int) -> int:
    if nums[-1] < target:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] >= target:
            return i


print(search_insert_idx(nums=[1, 3, 5, 6], target=7))
