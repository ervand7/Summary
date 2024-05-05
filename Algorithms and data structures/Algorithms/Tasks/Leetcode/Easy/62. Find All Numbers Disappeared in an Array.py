from typing import List


# my solution
def find_disappeared_numbers(nums: List[int]) -> List[int]:
    result = []
    s = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in s:
            result.append(i)

    return result
