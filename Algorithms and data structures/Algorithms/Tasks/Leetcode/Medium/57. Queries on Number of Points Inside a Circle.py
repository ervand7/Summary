from typing import List


def count_points(points: List[List[int]], queries: List[List[int]]) -> List[int]:
    result = []

    for x, y, radius in queries:
        count = 0
        for p in points:
            if pow(p[0] - x, 2) + pow(p[1] - y, 2) <= pow(radius, 2):
                count += 1

        result.append(count)

    return result
