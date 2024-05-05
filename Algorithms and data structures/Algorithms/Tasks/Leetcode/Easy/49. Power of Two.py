def is_power_of_two(n: int) -> bool:
    if n in {1, 2}:
        return True

    while n > 2:
        n /= 2
        if n == 2:
            return True

    return False


# ChatGPT solution
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
