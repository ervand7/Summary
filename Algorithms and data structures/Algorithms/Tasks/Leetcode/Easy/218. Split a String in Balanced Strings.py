# my solution
def balanced_string_split(s: str) -> int:
    result = 0
    r_count, l_count = 0, 0
    for i in s:
        if i == "R":
            r_count += 1
        else:
            l_count += 1

        if r_count == l_count:
            result += 1
            r_count = l_count = 0

    return result


# ChatGPT solution
def balanced_string_split(s: str) -> int:
    balance = 0
    count = 0

    for char in s:
        balance += 1 if char == 'R' else -1
        if balance == 0:
            count += 1

    return count
