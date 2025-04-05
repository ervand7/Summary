# my solution
# it can be solved without stack
# whenever you encounter a first '(' remove it and when ct of '(' == ct of ')' then remove ')'
def remove_outer_parentheses(s: str) -> str:
    count_open, count_close = 0, 0
    open_was_removed = False
    box = []
    for i in s:
        if i == "(":
            if not open_was_removed:
                open_was_removed = True
            else:
                box.append(i)
                count_open += 1

        elif i == ")":
            count_close += 1
            if 0 < count_close <= count_open:
                box.append(i)
            else:
                count_open = count_close = 0
                open_was_removed = False

    return "".join(box)


# ChatGPT solution
def remove_outer_parentheses(s: str) -> str:
    result = []
    balance = 0
    for char in s:
        if char == '(':
            if balance > 0:
                result.append(char)
            balance += 1
        else:  # char == ')'
            balance -= 1
            if balance > 0:
                result.append(char)
    return ''.join(result)


print(remove_outer_parentheses("(()())(())(()(()))"))
