from typing import List


# my solution
def sort_array_by_parity_II(nums: List[int]) -> List[int]:
    evens, odds = [], []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = evens.pop()
        else:
            nums[i] = odds.pop()

    return nums


# ChatGPT solution
def sort_array_by_parity_II(nums: List[int]) -> List[int]:
    n = len(nums)
    even_index, odd_index = 0, 1

    while even_index < n and odd_index < n:
        if nums[even_index] % 2 == 0:
            even_index += 2
        elif nums[odd_index] % 2 == 1:
            odd_index += 2
        else:
            nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
            even_index += 2
            odd_index += 2

    return nums


print(sort_array_by_parity_II([0, 2, 4, 6, 1, 3, 5, 7]))
