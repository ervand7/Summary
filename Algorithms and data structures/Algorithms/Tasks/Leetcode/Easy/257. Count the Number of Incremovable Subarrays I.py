from typing import List


# ChatGPT solution
def incremovable_subarray_count(nums: List[int]) -> int:
    def is_strictly_increasing(arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i, n):
            new_array = nums[:i] + nums[j + 1:]
            if is_strictly_increasing(new_array):
                count += 1

    return count


print(incremovable_subarray_count([6, 5, 7, 8]))
