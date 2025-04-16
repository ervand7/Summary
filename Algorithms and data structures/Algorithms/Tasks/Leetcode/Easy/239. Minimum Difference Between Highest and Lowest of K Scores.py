from typing import List


# my solution
def minimum_difference(nums: List[int], k: int) -> int:
    result = float('inf')
    nums.sort()
    for i in range(len(nums) - k + 1):
        slice = nums[i:i + k]
        diff = slice[-1] - slice[0]
        result = min([result, diff])

    return result


print(minimum_difference([90], 1))
