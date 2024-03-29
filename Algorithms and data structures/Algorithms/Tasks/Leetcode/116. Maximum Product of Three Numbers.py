from typing import List


def maximum_product(nums: List[int]) -> int:
    # First, sort the nums array
    nums.sort()
    # The maximum product can be either:
    # 1. Product of the last three numbers (all positive)
    # 2. Product of the first two (could be negative and thus bigger when multiplied) and the last one (biggest positive)
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
