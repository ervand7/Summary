from typing import List


# my solution
def construct_rectangle(area: int) -> List[int]:
    # find all divisors of area
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


#  ChatGPT solution
def construct_rectangle(area: int) -> List[int]:
    # Start with the square root of the area, because the closer L and W are to each
    # other, the smaller the difference between them will be (L >= W).
    w = int(area ** 0.5)

    # Decrease W until you find a width that exactly divides the area,
    # ensuring L >= W and the area is exactly area.
    while area % w != 0:
        w -= 1

    # Calculate L based on the width W found.
    l = area // w

    return [l, w]


construct_rectangle(256)
