# my solution
def count_binary_substrings(s: str) -> int:
    if len(s) < 2:
        return 0

    result = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result += 1

            p1 = i - 2
            p2 = i + 1
            low_val = s[i - 1]
            high_val = s[i]
            while p1 >= 0 and p2 < len(s):
                if s[p1] == low_val and s[p2] == high_val:
                    result += 1
                    p1 -= 1
                    p2 += 1
                else:
                    break

    return result
