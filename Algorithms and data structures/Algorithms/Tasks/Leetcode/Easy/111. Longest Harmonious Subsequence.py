from typing import List


# my solution
def find_LHS(nums: List[int]) -> int:
    nums.sort()
    h_table = {}
    for i in nums:
        h_table[i] = h_table.get(i, 0) + 1

    result = 0
    for i in h_table:
        if i + 1 in h_table:
            result = max([result, h_table[i] + h_table[i + 1]])

    return result
