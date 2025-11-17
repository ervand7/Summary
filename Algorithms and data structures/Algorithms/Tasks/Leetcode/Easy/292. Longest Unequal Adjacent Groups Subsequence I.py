from typing import List


# my solution
def get_longest_subsequence(words: List[str], groups: List[int]) -> List[str]:
    current = groups[0]
    result = [words[0]]
    for i in range(1, len(words)):
        if groups[i] != current:
            result.append(words[i])
            current = groups[i]

    return result
