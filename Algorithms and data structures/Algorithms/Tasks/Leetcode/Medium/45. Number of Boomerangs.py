from collections import defaultdict
from typing import List


def number_of_boomerangs(points: List[List[int]]) -> int:
    res = 0
    for i in points:
        distance_count = defaultdict(int)
        for j in points:
            if i == j:
                continue
            # squared distance (no need for sqrt)
            dx = i[0] - j[0]
            dy = i[1] - j[1]
            dist = dx * dx + dy * dy
            distance_count[dist] += 1

        for count in distance_count.values():
            res += count * (count - 1)
    return res


print(number_of_boomerangs([[0, 0], [1, 0], [2, 0]]))
