from typing import List


def hash_table(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


print(hash_table([2, 7, 11, 15], 9))  # [1, 0]
