from typing import List


# my solution
def find_max_consecutive_ones(nums: List[int]) -> int:
    if not nums:
        return 0

    result = 0
    counter = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            counter += 1
            if i == len(nums) - 1:
                if counter > result:
                    result = counter
        else:
            if counter > result:
                result = counter
            counter = 0

    return result
