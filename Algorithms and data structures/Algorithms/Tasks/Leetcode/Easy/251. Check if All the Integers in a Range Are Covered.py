from typing import List


# my solution
def is_covered(ranges: List[List[int]], left: int, right: int) -> bool:
    for i in range(left, right + 1):
        covered = False
        for l, r in ranges:
            if l <= i <= r:
                covered = True
                break

        if not covered:
            return False

    return True


print(is_covered(ranges=[[1, 10], [10, 20]], left=21, right=21))
