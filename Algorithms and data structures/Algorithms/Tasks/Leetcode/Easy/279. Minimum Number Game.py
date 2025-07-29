import heapq
from typing import List


# my solution
def number_game(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    result = []
    while nums:
        result.extend([heapq.heappop(nums), heapq.heappop(nums)][::-1])

    return result
