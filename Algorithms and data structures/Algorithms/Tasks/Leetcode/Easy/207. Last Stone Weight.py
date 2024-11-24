from typing import List
import heapq


# my not optimal solution O(n2)
def last_stone_weight(stones: List[int]) -> int:
    if len(stones) == 1:
        return stones[0]
    if len(stones) == 2:
        return max(stones) - min(stones)

    while True:
        stones.sort(reverse=True)
        diff = stones[0] - stones[1]
        stones = [diff] + stones[2:]
        if len(stones) == 2:
            return max(stones) - min(stones)


# O(n*log n)
def last_stone_weight(stones: List[int]) -> int:
    # Convert stones to a max-heap by using negative weights
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        # Pop two heaviest stones
        first = -heapq.heappop(stones)
        second = -heapq.heappop(stones)

        if first != second:
            # Push the remaining weight back into the heap
            heapq.heappush(stones, -(first - second))

    # Return the last stone weight or 0 if no stones left
    return -stones[0] if stones else 0


last_stone_weight([2, 7, 4, 1, 8, 1])
