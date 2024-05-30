from typing import List


# my solution
def uncommon_from_sentences(s1: str, s2: str) -> List[str]:
    h1, h2 = {}, {}
    for i in s1.split():
        h1[i] = h1.get(i, 0) + 1

    for i in s2.split():
        h2[i] = h2.get(i, 0) + 1

    result = []
    for k, v in h1.items():
        if v == 1 and k not in h2:
            result.append(k)

    for k, v in h2.items():
        if v == 1 and k not in h1:
            result.append(k)

    return result
