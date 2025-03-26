from typing import List


# my solution (works bad for large array)
def max_area(height: List[int]) -> int:
    n = len(height)
    result = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if i != j:
                attempt = (j - i) * min(height[i], height[j])
                result = max(result, attempt)

    return result


# ChatGPT solution
def max_area(height: List[int]) -> int:
    result = 0
    left, right = 0, len(height) - 1
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        result = max(result, h * w)

        # Move the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result
