from typing import List


# My solution
def largest_perimeter(nums: List[int]) -> int:
    nums.sort(reverse=True)

    def find(shift: int = 0):
        result = 0
        # find a and b
        a_idx, b_idx = 0, 0
        a, b = 0, 0
        for i in range(1 + shift, len(nums)):
            if nums[i - 1] / nums[i] < 2.0:
                a_idx = i - 1
                b_idx = i
                a = nums[a_idx]
                b = nums[b_idx]
                break

        a_b_sum = a + b
        a_b_diff = a - b
        for c in nums[b_idx + 1:]:
            if a_b_diff < c < a_b_sum:
                return a_b_sum + c

        return result

    shift = 0
    while shift <= len(nums) - 3:
        res = find(shift)
        if res != 0:
            return res

        shift += 1

    return 0


# ChatGPT solution
def largest_perimeter(nums):
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:  # Check triangle inequality
            return nums[i] + nums[i + 1] + nums[i + 2]
    return 0  # No valid triangle found
