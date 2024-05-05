# my solution
def guess_number(n: int) -> int:
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        g = guess(mid)
        if g == 0:
            return mid
        if g == -1:
            high = mid - 1
        else:
            low = mid + 1


def guess(n: int):
    res = 77
    if n == res:
        return 0
    if n > res:
        return -1
    return 1


print(guess_number(77))
