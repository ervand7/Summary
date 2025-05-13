# my solution
def are_almost_equal(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    h1, h2 = {}, {}
    for i in range(len(s1)):
        h1[i] = s1[i]
        h2[i] = s2[i]

    not_matched = []
    for k, v in h1.items():
        if h2[k] != v:
            not_matched.append([k, h2[k]])

    if len(not_matched) != 2:
        return False

    not_matched[0][1], not_matched[1][1] = not_matched[1][1], not_matched[0][1]
    attempt = list(s2)
    for k, v in not_matched:
        attempt[k] = v

    return "".join(attempt) == s1


# ChatGPT solution
def are_almost_equal(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    diff = []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(i)

    if len(diff) != 2:
        return False

    i, j = diff
    return s1[i] == s2[j] and s1[j] == s2[i]
