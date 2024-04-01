from typing import List


# my solution
def find_error_nums(nums: List[int]) -> List[int]:
    h = {}
    nums.sort()
    for i in nums:
        if i in h:
            return [i, list(set(range(1, len(nums) + 1)) - set(nums))[0]]
        h[i] = True


# ChatGPT solution
def find_error_nums(nums: List[int]) -> List[int]:
    n = len(nums)
    # Calculate expected sums
    expected_sum = n * (n + 1) // 2
    expected_square_sum = n * (n + 1) * (2 * n + 1) // 6

    # Calculate actual sums
    actual_sum = sum(nums)
    actual_square_sum = sum(x ** 2 for x in nums)

    # Derive equations
    sum_diff = expected_sum - actual_sum  # Missing - Duplicate
    square_sum_diff = expected_square_sum - actual_square_sum  # Missing^2 - Duplicate^2

    # Solve the equations
    # (Missing + Duplicate) = square_sum_diff / sum_diff
    sum_plus = square_sum_diff // sum_diff

    # Now we have two equations:
    # sum_diff = Missing - Duplicate
    # sum_plus = Missing + Duplicate
    # Solving for Missing and Duplicate
    missing = (sum_diff + sum_plus) // 2
    duplicate = sum_plus - missing

    return [duplicate, missing]
