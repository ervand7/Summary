from typing import List
import heapq


# my solution
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    h = []
    for x, y in points:
        val = (x * x + y * y) ** 0.5
        h.append([(x, y), val])

    h.sort(key=lambda x: x[1])
    return [i[0] for i in h][:k]


# ChatGPT solution
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    # Use a max-heap of size k (invert distance to simulate max-heap with min-heap)
    max_heap = []

    for x, y in points:
        dist = -(x * x + y * y)  # negate for max-heap
        heapq.heappush(max_heap, (dist, x, y))
        if len(max_heap) > k:
            heapq.heappop(max_heap)  # remove the farthest

    return [[x, y] for _, x, y in max_heap]
