def is_ugly(n: int) -> bool:
    if n <= 0:
        return False

    for i in [2, 3, 5]:
        while n % i == 0:
            n /= i

    return n == 1


print(is_ugly(14))


def is_ugly(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return is_ugly(n // 2)
    if n % 3 == 0:
        return is_ugly(n // 3)
    if n % 5 == 0:
        return is_ugly(n // 5)
    return False
