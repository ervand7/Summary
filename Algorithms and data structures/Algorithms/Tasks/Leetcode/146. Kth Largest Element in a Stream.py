import heapq
from typing import List


# ChatGPT solution
class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Create instance
kthLargest = KthLargest(3, [4, 5, 8, 2])

# Adding elements and printing results
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8


# my solution (slow)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        pointer = 0
        for i in self.nums:
            if val < i:
                break
            pointer += 1

        self.nums.insert(pointer, val)
        return self.nums[-self.k]
