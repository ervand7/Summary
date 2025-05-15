from typing import List


def is_prefix_string(s: str, words: List[str]) -> bool:
    len_s = len(s)
    len_words = len(words)
    attempt = ""
    i = 0
    while len(attempt) <= len_s:
        attempt += words[i]

        if i == (len_words - 1) and len(attempt) < len(s):
            return False

        i += 1

    i = 0
    while i < len(s):
        if s[i] != attempt[i]:
            return False

    return True


print(is_prefix_string("iloveleetcode", ["i", "love", "leetcode", "apples"]))
