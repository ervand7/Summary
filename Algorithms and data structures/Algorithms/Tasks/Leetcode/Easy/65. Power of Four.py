# my solution
def is_power_of_four(n: int) -> bool:
    if n == 1:
        return True

    i = 1
    while True:
        result = 4 ** i
        if result == n:
            return True
        if result > n:
            return False

        i += 1
