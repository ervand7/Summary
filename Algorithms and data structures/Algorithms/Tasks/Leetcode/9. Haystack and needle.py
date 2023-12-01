# мое решение
def find(haystack: str, needle: str) -> int:
    if not all([haystack, needle]):
        return -1

    for i in range(0, len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


print(find(haystack="qweqweqweq", needle="rtyuioz"))
