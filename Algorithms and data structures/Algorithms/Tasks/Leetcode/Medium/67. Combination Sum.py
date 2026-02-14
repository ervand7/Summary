from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int], remaining: int):
        if remaining == 0:
            result.append(current.copy())
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # reuse allowed
            current.pop()

    backtrack(0, [], target)
    return result


print(combination_sum(candidates=[2, 3, 6, 7], target=7))
