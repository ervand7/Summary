from typing import List
from pprint import pprint


# ChatGPT solution
def special_grid(n: int) -> List[List[int]]:
    def build(n, start):
        if n == 0:
            return [[start]]
        size = 2 ** (n - 1)
        quarter = size * size

        tr = build(n - 1, start)
        br = build(n - 1, start + quarter)
        bl = build(n - 1, start + 2 * quarter)
        tl = build(n - 1, start + 3 * quarter)

        res = []
        for i in range(size):
            res.append(tl[i] + tr[i])
        for i in range(size):
            res.append(bl[i] + br[i])
        return res

    return build(n, 0)


pprint(special_grid(1))
