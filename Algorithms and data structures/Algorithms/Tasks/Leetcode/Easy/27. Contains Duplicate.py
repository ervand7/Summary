from typing import List


# my solution
def contains_duplicate(nums: List[int]) -> bool:
    hash_table = {}
    for i in nums:
        if hash_table.get(i) is None:
            hash_table[i] = True
        else:
            return True

    return False
