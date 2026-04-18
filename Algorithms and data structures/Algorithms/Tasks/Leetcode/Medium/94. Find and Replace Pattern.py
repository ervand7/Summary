from typing import List


# Time: O(n * m)
# Space: O(m)
def find_and_replace_pattern(words: List[str], pattern: str) -> List[str]:
    unique_letters_len = len(set(pattern))

    def get_pattern(string: str) -> List[int]:
        h = {}
        i = 0
        for letter in string:
            if letter not in h:
                i += 1
                h[letter] = i

        result = []
        for letter in string:
            result.append(h[letter])

        return result

    p = get_pattern(pattern)
    len_p = len(p)

    def pattern_match(string: str) -> bool:
        h = {}
        i = 0
        for letter in string:
            if letter not in h:
                i += 1
                h[letter] = i

        if len(h) != unique_letters_len:
            return False

        for i in range(len_p):
            if h[string[i]] != p[i]:
                return False

        return True

    result = []
    for word in words:
        if pattern_match(word):
            result.append(word)

    return result


print(find_and_replace_pattern(["abcdefghijklab", "abcdefghijkabl"], "abcdefghijklab"))
