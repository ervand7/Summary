from typing import List


# my solution
def find_the_prefix_common_array(a: List[int], b: List[int]) -> List[int]:
    result = []
    for i in range(1, len(a) + 1):
        result.append(len(
            set(a[:i]) & set(b[:i])
        ))

    return result


def find_the_prefix_common_array(A: List[int], B: List[int]) -> List[int]:
    seenA = set()
    seenB = set()
    result = []
    common = 0

    for a, b in zip(A, B):
        seenA.add(a)
        seenB.add(b)

        if a in seenB:
            common += 1
        if b in seenA and b != a:
            common += 1

        result.append(common)

    return result
