import heapq


# ChatGPT solution
def nth_ugly_number(n: int) -> int:
    heap = [1]
    seen = {1}

    for _ in range(n):
        val = heapq.heappop(heap)
        for f in [2, 3, 5]:
            nxt = val * f
            if nxt not in seen:
                seen.add(nxt)
                heapq.heappush(heap, nxt)
    return val


print(nth_ugly_number(10))


# ChatGPT another solution
def nth_ugly_number(n: int) -> int:
    ugly_nums = [1]  # first ugly_nums number is 1
    idx2 = idx3 = idx5 = 0  # indexes for multiples of 2, 3, and 5

    while len(ugly_nums) < n:
        # next candidates
        next2 = ugly_nums[idx2] * 2
        next3 = ugly_nums[idx3] * 3
        next5 = ugly_nums[idx5] * 5

        # pick the smallest next ugly_nums number
        next_ugly = min(next2, next3, next5)
        ugly_nums.append(next_ugly)

        # move the pointer(s) that produced this value
        if next_ugly == next2:
            idx2 += 1
        if next_ugly == next3:
            idx3 += 1
        if next_ugly == next5:
            idx5 += 1

    return ugly_nums[-1]
