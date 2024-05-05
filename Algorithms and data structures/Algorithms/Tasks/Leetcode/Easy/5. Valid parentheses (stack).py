# my solution
def is_valid(data: str) -> bool:
    stack = []
    brackets = {"]": "[", ")": "(", "}": "{"}
    for i in data:
        if i in {"[", "(", "{"}:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if brackets[i] != stack.pop():
                return False

    return len(stack) == 0


print(is_valid("([{((([[({[[()]]})]])))}])"))
