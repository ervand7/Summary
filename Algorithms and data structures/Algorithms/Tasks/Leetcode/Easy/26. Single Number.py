from typing import List


# my solution
def single_number(nums: List[int]) -> int:
    hash_table = {}
    for i in nums:
        if hash_table.get(i) is None:
            hash_table[i] = 1
        else:
            del hash_table[i]

    return next(iter(hash_table))


print(single_number([1, 2, 3, 5, 4, 1, 2, 3, 4]))


# my old solution
def single_number(nums: List[int]) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i


print(single_number([1, 2, 3, 5, 4, 1, 2, 3, 4]))


# ChatGPT solution
def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


print(single_number([1, 2, 3, 5, 4, 1, 2, 3, 4]))