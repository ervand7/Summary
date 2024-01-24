# my solution
def arrange_coins(n: int) -> int:
    pointer = 1
    while True:
        n -= pointer
        if n < 0:
            return pointer - 1

        pointer += 1
