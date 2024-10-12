from typing import List


def findJudge(n: int, trust: List[List[int]]) -> int:
    if not trust:
        return n if n == 1 else -1

    h = {}
    h2 = {}
    for i in trust:
        key = i[1]
        h[key] = h.get(key, 0) + 1

        key = i[0]
        h2[key] = True

    # if len(h) > 1:
    #     return -1

    k = list(h.keys())[0]
    # if k in h2:
    #     return -1

    if h[k] != n - 1:
        return -1

    return k


print(findJudge(trust=[[1, 2], [1, 3], [2, 1], [2, 3], [1, 4], [4, 3], [4, 1]], n=4))
