def first_bad_version(n: int) -> int:
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


def is_bad_version(n):
    if n >= 83:
        return True
    return False


print(first_bad_version(100))
