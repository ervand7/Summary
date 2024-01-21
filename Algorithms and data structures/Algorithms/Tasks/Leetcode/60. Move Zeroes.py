from typing import List


# my solution
def move_zeroes(nums: List[int]) -> None:
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            while nums[j] == 0 and j < len(nums) - 1:
                j += 1

            nums[i], nums[j] = nums[j], nums[i]


# ChatGPT solution
def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
