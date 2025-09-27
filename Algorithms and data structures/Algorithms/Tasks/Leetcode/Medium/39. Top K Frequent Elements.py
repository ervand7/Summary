from typing import List


# my solution
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    h = {}
    for i in nums:
        h[i] = h.get(i, 0) + 1

    h_sorted = sorted(h.items(), key=lambda x: x[1], reverse=True)
    return [i[0] for i in h_sorted][:k]
