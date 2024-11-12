from typing import List


# my solution
def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    h = [(sum(row), i) for i, row in enumerate(mat)]
    return [i for _, i in sorted(h)[:k]]
