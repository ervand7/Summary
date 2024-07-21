from typing import List


# my solution
def smallest_ange_i(nums: List[int], k: int) -> int:
    minimum, maximum = min(nums), max(nums)

    if minimum + k >= maximum - k:
        return 0
    return (maximum - k) - (minimum + k)


# ChatGPT solution
def minimize_score(nums, k):
    if not nums:
        return 0

    max_val = max(nums)
    min_val = min(nums)

    # Calculate the minimum possible score
    min_score = max(0, (max_val - k) - (min_val + k))

    return min_score