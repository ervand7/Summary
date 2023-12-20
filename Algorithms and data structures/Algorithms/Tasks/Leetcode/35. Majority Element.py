from typing import List


# my solution
def majority_element(nums: List[int]) -> int:
    threshold = len(nums) // 2
    hash_table = {}
    for i in nums:
        hash_table[i] = hash_table.get(i, 0) + 1
        if hash_table[i] > threshold:
            return i
