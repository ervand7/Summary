from typing import List


# my solution
def minimum_operations(nums: List[int]) -> int:
    result = 0

    while True:
        while 0 in set(nums):
            nums.remove(0)

        if not nums:
            break

        minimum = min(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[i] -= minimum

        result += 1

    return result


# ChatGPT solution
def minimum_operations(nums):
    return len(set(nums) - {0})


minimum_operations([1, 5, 0, 3, 5])
