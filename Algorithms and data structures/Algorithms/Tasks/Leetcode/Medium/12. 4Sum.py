from typing import List


# correct but slow and out of timeout solution
def four_sum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    result = []

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        quadruplet = sorted([nums[a], nums[b], nums[c], nums[d]])
                        if quadruplet not in result:  # Avoid duplicates
                            result.append(quadruplet)

    return result


# fast ChatGpt solution
def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    results = []

    for i in range(n - 3):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Early termination
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break  # No need to proceed if the smallest possible sum is greater than target
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue  # No need to proceed if the largest possible sum is less than target
        for j in range(i + 1, n - 2):
            # Skip duplicates for the second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # Early termination
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    # Skip duplicates for the third and fourth numbers
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return results
