from typing import List


# O(n2)
def two_sum_simple(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == target - nums[j]:
                return [i, j]


two_sum_simple([2, 7, 11, 15], 9)


# O(n)
def two_pass_hash_table(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


two_pass_hash_table([2, 7, 11, 15], 9)


# O(n)
def one_pass_hash_table(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


one_pass_hash_table([2, 7, 11, 15], 9)
