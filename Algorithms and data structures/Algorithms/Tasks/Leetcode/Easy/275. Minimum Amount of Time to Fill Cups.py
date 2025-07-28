from typing import List


# my solution
def fill_cups(amount: List[int]) -> int:
    result = 0
    while any(amount):
        amount.sort()
        amount[-1] -= 1
        if amount[1] > 0:
            amount[1] -= 1

        result += 1

    return result
