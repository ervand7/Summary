from typing import List


# my solution
def find_k_distant_indices(nums: List[int], key: int, k: int) -> List[int]:
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if abs(i - j) <= k and nums[j] == key:
                result.add(i)

    return sorted(list(result))


# ChatGPT solution
def find_k_distant_indices(nums: List[int], key: int, k: int) -> List[int]:
    n = len(nums)
    marked = [False] * n

    for j in range(n):
        if nums[j] == key:
            start = max(0, j - k)
            end = min(n - 1, j + k)
            for i in range(start, end + 1):
                marked[i] = True

    return [i for i, val in enumerate(marked) if val]


print(find_k_distant_indices([3, 4, 9, 1, 3, 9, 5], 9, 1))
