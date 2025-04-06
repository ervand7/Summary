# my good solution
def remove_duplicates(s: str) -> str:
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    return "".join(stack)


# my bad and not effective solution
def remove_duplicates(s: str) -> str:
    if len(s) == 1:
        return s

    s = list(s)
    temp = []
    while True:
        i = 0
        has_duplicates = False
        while i < len(s):
            if i == len(s) - 1:
                temp.append(s[i])
                break
            if s[i] == s[i + 1]:
                has_duplicates = True
                i += 2
            else:
                temp.append(s[i])
                i += 1

        if not has_duplicates:
            break
        s = temp
        temp = []

    return "".join(s)
