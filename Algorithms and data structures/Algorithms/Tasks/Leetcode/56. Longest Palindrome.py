def longest_palindrome(s: str) -> int:
    h = {}
    has_odd = False
    for i in s:
        h[i] = h.get(i, 0) + 1

    result = 0
    for k, v in h.items():
        if v % 2 == 0:
            result += v
        else:
            result += v - 1
            has_odd = True

    if has_odd:
        result += 1

    return result
