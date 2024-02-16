from typing import List


# my solution
def construct_rectangle(area: int) -> List[int]:
    d = [area]
    for i in range(area // 2, 0, -1):
        temp = area // i
        if temp * i == area:
            d.append(i)
    i = 0
    j = len(d) - 1
    result = []
    while i <= j:
        if d[i] * d[j] == area:
            result = [d[i], d[j]]
            i += 1
            j -= 1
    return result
