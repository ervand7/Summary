import heapq
from typing import List


# my solution
def max_subsequence(nums: List[int], k: int) -> List[int]:
    h_nums = nums[:]
    heapq.heapify(h_nums)
    while len(h_nums) > k:
        heapq.heappop(h_nums)

    result = []
    for i in nums:
        if i in h_nums:
            result.append(i)
            h_nums.remove(i)

    return result


# my another solution
def max_subsequence(nums: List[int], k: int) -> List[int]:
    h_nums = sorted(nums, reverse=True)[:k]

    result = []
    for i in nums:
        if i in h_nums:
            result.append(i)
            h_nums.remove(i)

    return result


# ChatGPT solution
def max_subsequence(nums: List[int], k: int) -> List[int]:
    # Pair each number with its index
    indexed = [(num, i) for i, num in enumerate(nums)]

    # Sort by value descending, keep top k
    top_k = sorted(indexed, key=lambda x: -x[0])[:k]

    # Sort those k elements by original index to preserve order
    top_k_sorted = sorted(top_k, key=lambda x: x[1])

    return [num for num, _ in top_k_sorted]
