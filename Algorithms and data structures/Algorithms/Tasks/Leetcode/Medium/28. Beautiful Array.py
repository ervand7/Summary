from typing import List


def beautiful_array(n: int) -> List[int]:
    if n == 1:
        return [1]

    result = [1]
    while len(result) < n:
        temp = []
        for x in result:
            if 2 * x - 1 <= n:
                temp.append(2 * x - 1)  # make new odds
        for x in result:
            if 2 * x <= n:
                temp.append(2 * x)  # make new evens
        result = temp
    return result


print(beautiful_array(4))
