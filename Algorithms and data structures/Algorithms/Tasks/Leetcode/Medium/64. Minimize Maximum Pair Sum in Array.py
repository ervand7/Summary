from typing import List


def min_pair_sum(nums: List[int]) -> int:
    len_nums = len(nums)
    result = 0
    nums.sort()
    for i in range(len_nums // 2):
        left = nums[i]
        right = nums[len_nums - 1 - i]
        result = max(result, left + right)

    return result
