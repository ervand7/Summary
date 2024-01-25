# my solution
def first_uniq_char(s: str) -> int:
    h = {}
    for i in range(len(s)):
        h[s[i]] = h.get(s[i], 0) + 1

    for i in range(len(s)):
        if h[s[i]] == 1:
            return i

    return -1
