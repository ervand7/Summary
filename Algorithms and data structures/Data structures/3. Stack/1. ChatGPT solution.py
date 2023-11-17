def is_stack(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top = stack.pop()
            if bracket_map[char] != top:
                return False

    return len(stack) == 0


print(is_stack("(((([{}]))))"))
