from typing import List


# my solution
def k_length_apart(nums: List[int], k: int) -> bool:
    first = False
    count = 0
    for i in nums:
        if i == 1 and first is False:
            count = 0
            first = True
            continue

        if i == 0:
            count += 1
        else:
            if count < k:
                return False
            count = 0

    return True


def k_length_apart(nums, k):
    prev_index = -1
    for i, num in enumerate(nums):
        if num == 1:
            if prev_index != -1 and i - prev_index - 1 < k:
                return False
            prev_index = i
    return True


print(k_length_apart([0, 0, 0, 1, 0, 1], 2))
