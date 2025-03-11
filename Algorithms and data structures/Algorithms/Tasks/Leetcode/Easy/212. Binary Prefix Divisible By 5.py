from typing import List


# ChatGPT solution
def prefixes_div_by5(nums: List[int]) -> List[bool]:
    res = []
    result = 0
    for bit in nums:
        result = result * 2 + bit
        res.append(result % 5 == 0)
    return res
