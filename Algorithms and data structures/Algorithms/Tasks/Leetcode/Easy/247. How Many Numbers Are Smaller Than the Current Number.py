from typing import List


# my effective solution
def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    h = {i: 0 for i in nums}
    sorted_nums = sorted(nums, reverse=True)
    for i in range(len(nums) - 1):
        if sorted_nums[i] > sorted_nums[i + 1]:
            h[sorted_nums[i]] = len_nums - i - 1

    return [h[i] for i in nums]


# my not effective solution
def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    for i in range(n):
        for j in range(n):
            if nums[j] < nums[i]:
                result[i] += 1

    return result


# ChatGPT solution:
def smaller_numbers_than_current(nums):
    # Step 1: Sort the array with original indices
    sorted_nums = sorted(nums)

    # Step 2: Map each number to its first occurrence index (i.e., count of smaller numbers)
    smaller_count = {}
    for i, num in enumerate(sorted_nums):
        if num not in smaller_count:
            smaller_count[num] = i  # first occurrence index = count of smaller numbers

    # Step 3: Build the result using the map
    return [smaller_count[num] for num in nums]


print(smaller_numbers_than_current([6, 5, 5, 4]))
