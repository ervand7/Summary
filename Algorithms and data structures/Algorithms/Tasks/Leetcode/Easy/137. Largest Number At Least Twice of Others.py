from typing import List


# my solution
def dominant_index(nums: List[int]) -> int:
    max_val = 0
    prev_max_val = 0
    idx = 0
    for i in range(len(nums)):
        if nums[i] > max_val:
            prev_max_val = max_val
            max_val = nums[i]
            idx = i
        else:
            if nums[i] > prev_max_val:
                prev_max_val = nums[i]

    return idx if max_val / 2 >= prev_max_val else -1


print(dominant_index([0, 0, 3, 2]))
