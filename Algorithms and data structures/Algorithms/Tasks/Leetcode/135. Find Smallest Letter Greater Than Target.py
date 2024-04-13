from typing import List


# my solution (is acceptable even we have not ordered list)
def next_greatest_letter(letters: List[str], target: str) -> str:
    diff = float("inf")
    result = ""
    not_found = True
    ord_target = ord(target)
    for i in letters:
        _diff = ord(i) - ord_target
        if 0 < _diff < diff:
            not_found = False
            diff = _diff
            result = i

    return letters[0] if not_found else result


# ChatGPT solution (only for sorted list)
def next_greatest_letter(letters, target):
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]
