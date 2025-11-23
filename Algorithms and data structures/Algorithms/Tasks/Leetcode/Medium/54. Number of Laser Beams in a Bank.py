from typing import List


# my solution
def number_of_beams(bank: List[str]) -> int:
    result = prev = next = 0
    for row in bank:
        count = sum([int(i) for i in row])
        if count > 0:
            if prev == 0:
                prev = count
                continue

            if next == 0:
                next = count
                result += (prev * next)
                prev = next
                next = 0

    return result


# ChatGPT solution
def number_of_beams(bank):
    prev = 0
    result = 0

    for row in bank:
        count = row.count('1')
        if count > 0:
            result += prev * count
            prev = count
    return result
