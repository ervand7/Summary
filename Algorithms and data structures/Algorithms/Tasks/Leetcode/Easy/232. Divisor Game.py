# my solution
def divisor_game(n: int) -> bool:
    i = -1
    x = 1
    while 0 < x < n and n % x == 0:
        i += 1
        n = n - x

    return i % 2 == 0
