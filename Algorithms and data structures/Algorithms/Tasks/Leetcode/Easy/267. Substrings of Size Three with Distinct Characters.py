# my solution
def count_good_substrings(s: str) -> int:
    n = len(s)
    result = 0
    if n < 3:
        return result

    for i in range(len(s) - 2):
        sub = s[i: i + 3]
        if len(set(sub)) == 3:
            result += 1

    return result
