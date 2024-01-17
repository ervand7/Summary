# my solution
def repeated_substring_pattern(s: str) -> bool:
    if s[:len(s) // 2] == s[len(s) // 2:]:
        return True

    for i in range(3, 11111, 2):
        if len(s) % i == 0:
            if s == s[:len(s) // i] * i:
                return True
    return False


def repeated_substring_pattern(s: str) -> bool:
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = s[:i]

            if substring * (n // i) == s:
                return True

    return False
