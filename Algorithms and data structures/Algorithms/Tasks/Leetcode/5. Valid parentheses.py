# my solution
def isValid(brackets: str) -> bool:
    stack = []
    is_good = True
    for i in brackets:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                is_good = False
                break
            last = stack.pop()
            if last == '(' and i == ')':
                continue
            if last == '[' and i == ']':
                continue
            if last == '{' and i == '}':
                continue
            is_good = False
            break
    if is_good and len(stack) == 0:
        return True
    else:
        return False


# more faster solution
def more_faster(brackets: str) -> bool:
    openBrackets = ['{', '[', '(']
    stack = []
    for i in brackets:
        if i in openBrackets:
            stack.append(i)
        elif stack:
            if i == ']' and stack[-1] != '[':
                return False
            if i == '}' and stack[-1] != '{':
                return False
            if i == ')' and stack[-1] != '(':
                return False
            stack.pop()
        else:
            return False
    return len(stack) == 0


more_faster('(((([{}]))))')
