from typing import List


# Given an integer array nums sorted in non-decreasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order of
# the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you
# need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique
# elements in the order they were present in nums initially. The remaining elements
# of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of
# nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of
# nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# O(n)
def remove_duplicates(nums: List[int]) -> int:
    pointer = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[pointer] = nums[i]
            pointer += 1
    return pointer


arr = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 5, 5, 4, 3, 2, 1]
print(remove_duplicates(arr))
print(arr)


# --------------------------------------------------------
# my solution
# O(n)
def remove_duplicates(arr: list) -> int:
    pointer = 0
    hash_table = {}
    for i in range(len(arr)):
        if arr[i] not in hash_table:
            hash_table[arr[i]] = pointer
            pointer += 1
    for key, idx in hash_table.items():
        arr[idx] = key
    return len(hash_table)


a = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 5, 5, 4, 3, 2, 1]
print(hex(id(a)))  # 0x7fdf78283940
remove_duplicates(a)
print(a)
print(hex(id(a)))  # 0x7fdf78283940
