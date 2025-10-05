from typing import List


def max_sum(nums: List[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)

    result = nums[0]
    for i in nums[1:]:
        if (result + i) > result:
            result += i
        else:
            return result

    return result
