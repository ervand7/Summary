from typing import List


# my solution
def distribute_candies(candies: int, num_people: int) -> List[int]:
    result = [0] * num_people
    i = 0
    count = 1
    while candies > 0:
        idx = i % num_people
        amount_to_increase = count if candies - count >= 0 else candies
        result[idx] += amount_to_increase

        candies -= count
        i += 1
        count += 1

    return result
