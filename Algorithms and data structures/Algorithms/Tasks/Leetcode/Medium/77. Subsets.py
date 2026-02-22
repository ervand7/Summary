from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


print(subsets(nums=[1, 2, 3]))
