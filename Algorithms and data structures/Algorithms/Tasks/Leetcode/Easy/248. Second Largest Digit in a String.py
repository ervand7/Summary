# my solution
def second_highest(s: str) -> int:
    values = []
    for i in s:
        if i.isnumeric():
            values.append(int(i))

    values = sorted(list(set(values)), reverse=True)
    if len(values) in {0, 1} or values[0] == values[1]:
        return -1

    return values[1]


# ChatGPT solution
def second_highest(s):
    digits = {int(c) for c in s if c.isdigit()}
    sorted_digits = sorted(digits, reverse=True)
    return sorted_digits[1] if len(sorted_digits) >= 2 else -1
