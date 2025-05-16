from typing import List


# my solution
def find_indices(nums: List[int], index_difference: int, value_difference: int):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if abs(i - j) >= index_difference and abs(nums[i] - nums[j]) >= value_difference:
                return [i, j]
    return [-1, -1]
