from typing import List


# O(n2)
def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == target - nums[j]:
                return [i, j]


print(two_sum([2, 7, 11, 15], 9))


# O(n)
# using hash table
def two_sum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        guess = target - nums[i]
        if guess in hash_table:
            return [hash_table[guess], i]
        hash_table[nums[i]] = i


print(two_sum([2, 7, 11, 15], 9))
