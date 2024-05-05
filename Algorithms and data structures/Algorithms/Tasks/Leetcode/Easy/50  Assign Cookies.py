from typing import List


# my solution
def find_content_children(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    to_ignore = set()
    result = 0
    for i in s:
        for j in range(len(g)):
            if j not in to_ignore:
                if i >= g[j]:
                    result += 1
                    to_ignore.add(j)
                    break
    return result


# ChatGPT solution
def find_content_children(g, s):
    g.sort()
    s.sort()
    i = 0
    j = 0
    result = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            result += 1
            i += 1
        j += 1

    return result
