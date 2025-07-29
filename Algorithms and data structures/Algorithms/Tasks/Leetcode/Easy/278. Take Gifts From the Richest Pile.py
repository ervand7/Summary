import heapq
import math
from typing import List


# my solution
def pick_gifts(gifts: List[int], k: int) -> int:
    for _ in range(k):
        gifts.sort()
        gifts.append(
            int(gifts.pop() ** 0.5)
        )

    return sum(gifts)


# ChatGPT solution
def pick_gifts(gifts, k):
    # Use negative values to simulate max-heap
    max_heap = [-g for g in gifts]
    heapq.heapify(max_heap)

    for _ in range(k):
        largest = -heapq.heappop(max_heap)
        reduced = int(math.sqrt(largest))
        heapq.heappush(max_heap, -reduced)

    # Return sum of remaining gifts (invert back to positive)
    return -sum(max_heap)
