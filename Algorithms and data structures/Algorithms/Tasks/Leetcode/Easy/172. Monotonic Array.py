from typing import List


# my solution
def is_monotonic(nums: List[int]) -> bool:
    if len(nums) <= 2:
        return True

    movement = None
    first = True
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if first:
                movement = 'encrease' if nums[i] > nums[i - 1] else 'decrease'
                first = False
                continue

            if movement == 'encrease':
                if nums[i] < nums[i - 1]:
                    return False
            else:
                if nums[i] > nums[i - 1]:
                    return False

    return True


# ChatGPT solution
def is_monotonic(nums: List[int]) -> bool:
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing
