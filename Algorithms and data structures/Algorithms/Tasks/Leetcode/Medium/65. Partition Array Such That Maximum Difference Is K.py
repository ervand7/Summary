from typing import List


def partition_array(nums: List[int], k: int) -> int:
    result = 1
    start = 0
    nums.sort(reverse=True)
    for i in range(1, len(nums)):
        if nums[start] - nums[i] > k:
            result += 1
            start = i

    return result
