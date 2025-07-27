# my solution
from typing import List


def find_relative_ranks(score: List[int]) -> List[str]:
    score_sorted = sorted(score, reverse=True)

    h = {}
    for idx, i in enumerate(score_sorted):
        h[i] = idx

    result = []
    for i in score:
        place = h[i]
        if place == 0:
            result.append("Gold Medal")
        elif place == 1:
            result.append("Silver Medal")
        elif place == 2:
            result.append("Bronze Medal")
        else:
            result.append(str(place + 1))

    return result

# ChatGPT solution
def find_relative_ranks(score):
    sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
    result = [""] * len(score)

    for rank, (idx, _) in enumerate(sorted_scores):
        if rank == 0:
            result[idx] = "Gold Medal"
        elif rank == 1:
            result[idx] = "Silver Medal"
        elif rank == 2:
            result[idx] = "Bronze Medal"
        else:
            result[idx] = str(rank + 1)

    return result
