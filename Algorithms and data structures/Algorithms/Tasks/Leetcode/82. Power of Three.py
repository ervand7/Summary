def is_power_of_three(n: int) -> bool:
    if n == 1:
        return True

    i = 1
    while True:
        result = 3 ** i
        if result == n:
            return True
        if result > n:
            return False

        i += 1
