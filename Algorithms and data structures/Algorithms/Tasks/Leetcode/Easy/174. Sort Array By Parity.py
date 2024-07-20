from typing import List


def sort_array_by_parity(nums: List[int]) -> List[int]:
    evens, odds = [], []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return evens + odds
