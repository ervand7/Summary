from typing import List


# my solution
def has_groups_size_x(deck: List[int]) -> bool:
    h = {}
    for i in deck:
        h[i] = h.get(i, 0) + 1

    values = h.values()

    for i in range(2, 10):
        if all([j % i == 0 for j in values]):
            return True

    return False


# ChatGPT solution
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def has_groups_size_x(deck: List[int]) -> bool:
    h = {}
    for i in deck:
        h[i] = h.get(i, 0) + 1

    values = list(h.values())

    # Compute the GCD of the frequencies
    freq_gcd = values[0]
    for value in values[1:]:
        freq_gcd = gcd(freq_gcd, value)
        if freq_gcd == 1:
            return False

    return freq_gcd > 1


def test_gcd():
    assert gcd(10, 5) == 5
    assert gcd(14, 21) == 7
    assert gcd(10, 3) == 1


test_gcd()

print(has_groups_size_x([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
