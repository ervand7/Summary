from typing import List


def distribute_candies(candy_type: List[int]) -> int:
    return len(list(set(candy_type))[:len(candy_type) // 2])
