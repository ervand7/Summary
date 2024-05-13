# my solution
def length_of_longest_substring(s: str) -> int:
    result = 0
    len_s = len(s)
    for i in range(len_s):
        if len_s - i <= result:
            break

        data = set()
        for j in range(i, len_s):
            if s[j] in data:
                result = max(result, len(data))
                break

            data.add(s[j])
            if j == len_s - 1:
                result = max(result, len(data))

    return result


# ChatGPT solution
def length_of_longest_substring(s: str) -> int:
    char_map = {}
    start = 0
    result = 0

    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        result = max(result, i - start + 1)

    return result


print(length_of_longest_substring("abcabcbb"))
