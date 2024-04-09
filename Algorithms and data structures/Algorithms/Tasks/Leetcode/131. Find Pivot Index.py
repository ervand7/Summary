from typing import List


# my solution
def pivot_index(nums: List[int]) -> int:
    len_nums = len(nums)
    left_sum = 0
    right_sum = sum(nums[1:])
    for i in range(len_nums):
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
        if i < len_nums - 1:
            right_sum -= nums[i + 1]
        else:
            break

    return -1
