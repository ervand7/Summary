# my solution O(n^2)
def maximum_length_substring(s: str) -> int:
    max_len = 0
    len_s = len(s)

    for i in range(len_s - 1):
        sub = s[i]
        h = {s[i]: 1}
        for j in range(i + 1, len_s):
            h[s[j]] = h.get(s[j], 0) + 1
            if h.get(s[j], 0) > 2:
                break

            sub += s[j]
            max_len = max(max_len, len(sub))

    return max_len


# ChatGPT solution O(n)
def maximum_length_substring(s: str) -> int:
    h = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        h[char] = h.get(char, 0) + 1

        # If any character appears more than 2 times, shrink window from the left
        while h[char] > 2:
            left_char = s[left]
            h[left_char] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


print(maximum_length_substring("bcbbbcba"))
