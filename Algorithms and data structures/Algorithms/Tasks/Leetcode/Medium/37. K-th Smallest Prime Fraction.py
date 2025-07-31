import heapq
from typing import List


# my solution
def kth_smallest_prime_fraction(arr: List[int], k: int) -> List[int]:
    data = []
    heapq.heapify(data)
    len_arr = len(arr)
    for i in range(len_arr - 1):
        for j in range(i + 1, len_arr):
            val = arr[i] / arr[j]
            heapq.heappush(data, (-val, arr[i], arr[j]))
            if len(data) > k:
                heapq.heappop(data)

    result = heapq.heappop(data)[1:]
    return result
