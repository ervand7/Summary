from typing import List


def findIndices(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    nums.sort()
    i = 0
    j = len(nums) - 1
    while i <= j:
        if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
            return [i, j]

        i += 1
        j -= 1

    return [-1, -1]


print(findIndices([2, 8, 0], 2, 7))
