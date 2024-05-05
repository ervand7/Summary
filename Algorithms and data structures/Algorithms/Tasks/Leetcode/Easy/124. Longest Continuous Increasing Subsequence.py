from typing import List


# my solution
def find_length_of_LCIS(nums: List[int]) -> int:
    if len(nums) in {0, 1}:
        return len(nums)

    result = 1
    count = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
            result = max(result, count)
        else:
            count = 1

    return result
