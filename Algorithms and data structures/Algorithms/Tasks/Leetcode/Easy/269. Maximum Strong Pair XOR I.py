from typing import List


# my solution
def maximum_strong_pair_xor(nums: List[int]) -> int:
    result = 0
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if 0 < nums[i] - nums[j] <= min(nums[i], nums[j]):
                result = max(result, nums[i] ^ nums[j])

    return result
