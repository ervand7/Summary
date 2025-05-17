from typing import List


# my solution
def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    if k == 0:
        return [0] * n

    result = []
    for i in range(len(code)):
        new_element = 0
        if k > 0:
            diapason = range(1, k + 1)
        else:
            diapason = range(-1, k - 1, -1)

        for j in diapason:
            idx = (i + j) % n
            new_element += code[idx]

        result.append(new_element)

    return result
