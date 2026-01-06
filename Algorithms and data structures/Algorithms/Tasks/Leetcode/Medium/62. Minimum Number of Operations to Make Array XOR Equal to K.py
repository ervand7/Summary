from typing import List


def min_operations(nums: List[int], k: int) -> int:
    x = 0
    for n in nums:
        x ^= n
    return bin(x ^ k).count("1")


print(min_operations(nums=[2, 1, 3, 4], k=1))
