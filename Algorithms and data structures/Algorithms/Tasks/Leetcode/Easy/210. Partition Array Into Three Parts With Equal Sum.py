from typing import List


# ChatGPT solution
def can_three_parts_equal_sum(arr: List[int]) -> bool:
    total = sum(arr)
    # If the total sum is not divisible by 3, return False
    if total % 3 != 0:
        return False

    target = total // 3
    current_sum = 0
    partitions = 0

    # We iterate through the array and try to form segments with sum equal to target.
    # We only need to find two segments because the third is implied.
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == target:
            partitions += 1
            current_sum = 0
            # If we've found two segments and we are not at the last element,
            # then the remaining elements form the third segment.
            if partitions == 2 and i < len(arr) - 1:
                return True
    return False
