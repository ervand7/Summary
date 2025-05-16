from typing import List


# my solution
def distinct_averages(nums: List[int]) -> int:
    nums.sort()
    averages = set()
    i = 0
    j = len(nums) - 1
    while i < j:
        avg = (nums[i] + nums[j]) / 2
        averages.add(avg)
        i += 1
        j -= 1

    return len(averages)
