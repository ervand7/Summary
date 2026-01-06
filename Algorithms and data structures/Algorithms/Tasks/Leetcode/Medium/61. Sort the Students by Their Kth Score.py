from typing import List


def sort_the_students(score: List[List[int]], k: int) -> List[List[int]]:
    return sorted(score, key=lambda row: row[k], reverse=True)


# in-place solution
def sort_the_students(score: List[List[int]], k: int) -> None:
    score.sort(key=lambda row: row[k], reverse=True)
