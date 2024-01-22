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
def is_subsequence(s, t):
    pointer_s, pointer_t = 0, 0
    while pointer_s < len(s) and pointer_t < len(t):
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
        pointer_t += 1
    return pointer_s == len(s)
