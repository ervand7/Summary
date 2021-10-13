def define_stack(brackets: str):
    stack = []
    is_good = True
    for i in brackets:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                is_good = False
                break
            deleted_open_bracket = stack.pop()
            if deleted_open_bracket == '(' and i == ')':
                continue
            if deleted_open_bracket == '[' and i == ']':
                continue
            if deleted_open_bracket == '{' and i == '}':
                continue
            is_good = False
            break
    if is_good and len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


# print(define_stack('(((([{}]))))'))
