from typing import List


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# my solution
def minimum_pair_removal(nums: List[int]) -> int:
    count = 0

    while not is_sorted(nums):
        min_sum = float("inf")
        idx = 0
        for i in range(len(nums) - 1):
            summa = nums[i] + nums[i + 1]
            if summa < min_sum:
                min_sum = summa
                idx = i

        nums[idx:idx + 2] = [min_sum]
        count += 1

    return count
