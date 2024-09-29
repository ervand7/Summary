# my solution
def is_long_pressed_name(name: str, typed: str) -> bool:
    if name[0] != typed[0]:
        return False

    i, j = 0, 0
    last = -1
    while i < len(name) and j < len(typed):
        if name[i] == typed[j]:
            last = i
            i += 1
            j += 1
            continue
        if name[last] == typed[j]:
            j += 1
            continue
        return False

    return len(set(typed[j - 1:])) == 1 and i == len(name)


# ChatGPT solution
def is_long_pressed_name(name: str, typed: str) -> bool:
    i, j = 0, 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    return i == len(name)
