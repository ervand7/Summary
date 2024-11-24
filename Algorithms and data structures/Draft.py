from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    count = 0
    allowed = set(allowed)
    for i in words:
        if set(i)  == allowed:
            count += 1

    return count


print( countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
