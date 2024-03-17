# my solution
def is_subsequence(s: str, t: str) -> bool:
    s = list(s)
    t = list(t)
    insert_pos = 0
    t_start = 0
    for i in range(len(s)):
        for j in range(t_start, len(t)):
            t_start += 1
            if s[i] == t[j]:
                t[insert_pos] = s[i]
                insert_pos += 1

                if t[j] == t[-1] and i < len(s) - 1:
                    return False
                break

    return s == t[:len(s)]


# ChatGPT solution
def is_subsequence(sub, string):
    i, j = 0, 0
    while i < len(sub) and j < len(string):
        if sub[i] == string[j]:
            i += 1
        j += 1
    return i == len(sub)


print(is_subsequence("qwe1", "qweasdzxc"))
