from typing import List


# my solution (iterative)
def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# my solution (recursive)
def search(nums: List[int], target: int) -> int:
    result = -1

    def rec(low: int, high: int) -> None:
        nonlocal result
        if low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                result = mid
                return

            if nums[mid] > target:
                rec(low, mid - 1)
            else:
                rec(mid + 1, high)

    rec(0, len(nums) - 1)
    return result
