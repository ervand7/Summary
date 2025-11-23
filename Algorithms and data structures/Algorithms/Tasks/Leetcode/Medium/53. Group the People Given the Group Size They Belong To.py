from typing import List


# my solution
def group_the_people(group_sizes: List[int]) -> List[List[int]]:
    h = {}
    for idx, i in enumerate(group_sizes):
        if h.get(i) is None:
            h[i] = []
        h[i].append(idx)

    result = []
    for count, indexes in h.items():
        offset = 0
        for _ in range(len(indexes) // count):
            result.append(indexes[offset:offset + count])
            offset += count

    return result
