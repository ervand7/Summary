from typing import List


def maxSubArray(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
