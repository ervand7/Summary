from typing import List


# ChatGPT solution
def next_permutation(nums: List[int]) -> None:
    n = len(nums)
    pivot = -1

    # Step 1: Find the pivot
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break

    if pivot == -1:  # If no pivot found, reverse the entire array
        nums.reverse()
        return

    # Step 2: Find the smallest larger element
    for j in range(n - 1, pivot, -1):
        if nums[j] > nums[pivot]:
            # Step 3: Swap pivot with this element
            nums[pivot], nums[j] = nums[j], nums[pivot]
            break

    # Step 4: Reverse the suffix
    nums[pivot + 1:] = reversed(nums[pivot + 1:])


next_permutation([7, 6, 5, 4, 3, 1, 2])
