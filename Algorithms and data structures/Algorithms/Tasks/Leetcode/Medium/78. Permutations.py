from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in nums:
            if num in path:
                continue

            path.append(num)
            backtrack(path)
            path.pop()

    backtrack([])
    return result


print(permute([1, 2, 3]))
