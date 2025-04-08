# my solution
def gcd_of_strings(str1: str, str2: str) -> str:
    small, big = (str1, str2) if len(str1) <= len(str2) else (str2, str1)

    attempt = small
    while len(attempt) > 0:
        quotient_big = len(big) // len(attempt)
        quotient_small = len(small) // len(attempt)
        if (len(big) % len(attempt) == 0 and
                attempt * quotient_big == big and
                len(small) % len(attempt) == 0 and
                attempt * quotient_small == small):
            return attempt

        attempt = attempt[:-1]

    return ""


# ChatGPT solution
def gcd_of_strings(str1: str, str2: str) -> str:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if str1 + str2 != str2 + str1:
        return ""
    gcd_len = gcd(len(str1), len(str2))
    return str1[:gcd_len]


print(gcd_of_strings("QWERTYQWERTY", "QWERTYQWERTYQWERTY"))
