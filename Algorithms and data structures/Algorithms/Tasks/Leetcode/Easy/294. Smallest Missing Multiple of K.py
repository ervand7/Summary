from typing import List


def missing_multiple(nums: List[int], k: int) -> int:
    nums = set(nums)
    start = k
    while True:
        if start not in nums:
            return start
        start += k
