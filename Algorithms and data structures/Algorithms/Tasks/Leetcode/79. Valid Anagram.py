# my solution
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    h1, h2 = {}, {}
    for i in range(len(s)):
        h1[s[i]] = h1.get(s[i], 0) + 1
        h2[t[i]] = h2.get(t[i], 0) + 1

    for k, v in h1.items():
        if h2.get(k, 0) != v:
            return False

    return True
