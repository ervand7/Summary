# my solution
def word_pattern(pattern: str, s: str) -> bool:
    s_split = s.split()
    if len(pattern) != len(s_split):
        return False

    h1, h2 = {}, {}
    pattern_digits, s_digits = [], []
    pattern_pointer, s_pointer = 0, 0
    for i in range(len(pattern)):
        val = h1.get(pattern[i])
        if not val:
            pattern_pointer += 1
            h1[pattern[i]] = pattern_pointer
        pattern_digits.append(h1[pattern[i]])

        val = h2.get(s_split[i])
        if not val:
            s_pointer += 1
            h2[s_split[i]] = s_pointer
        s_digits.append(h2[s_split[i]])

    return pattern_digits == s_digits
