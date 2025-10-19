from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    h = {}
    for i in strs:
        val = "".join(sorted(i))
        if h.get(val) is None:
            h[val] = [i]
        else:
            h[val].append(i)

    return list(h.values())
