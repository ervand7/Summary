import heapq


# ChatGPT solution
def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
