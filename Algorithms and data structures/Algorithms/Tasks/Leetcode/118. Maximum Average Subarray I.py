from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    # Calculate the sum of the first k elements
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window through the array
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    # Calculate and return the maximum average
    return max_sum / k
