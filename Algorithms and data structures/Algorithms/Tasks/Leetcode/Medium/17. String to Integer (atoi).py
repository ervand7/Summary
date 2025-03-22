# ChatGPT solution
def my_atoi(s: str) -> int:
    int_min, int_max = -2 ** 31, 2 ** 31 - 1

    i = 0
    n = len(s)
    # 1. Skip leading whitespaces
    while i < n and s[i] == ' ':
        i += 1

    # Edge case: string contains only spaces
    if i == n:
        return 0

    # 2. Handle optional sign
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1

    # 3. Read digits
    num = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # 4. Check for overflow before adding
        if num > (int_max - digit) // 10:
            return int_max if sign == 1 else int_min

        num = num * 10 + digit
        i += 1

    return sign * num
