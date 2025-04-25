from typing import List


def get_no_zero_integers(n: int) -> List[int]:
    i = 1
    while True:
        if "0" in str(n - i) or "0" in str(i):
            i += 1
            continue
        else:
            return [n - i, i]
