from typing import List


# my solution
def array_rank_transform(arr: List[int]) -> List[int]:
    h = {}
    for k, v in enumerate(sorted(set(arr)), 1):
        h[v] = k

    return [h[k] for k in arr]
