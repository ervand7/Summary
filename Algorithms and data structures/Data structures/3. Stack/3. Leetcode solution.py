def solution(brackets: str) -> bool:
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


print(solution('(((([{}]))))'))
