from typing import List


# my solution
def find_relative_ranks(score: List[int]) -> List[str]:
    s = sorted(score, reverse=True)
    h = {}
    for i in range(len(s)):
        if i == 0:
            h[s[i]] = "Gold Medal"
        elif i == 1:
            h[s[i]] = "Silver Medal"
        elif i == 2:
            h[s[i]] = "Bronze Medal"
        else:
            h[s[i]] = str(i + 1)

    return [h[i] for i in score]
