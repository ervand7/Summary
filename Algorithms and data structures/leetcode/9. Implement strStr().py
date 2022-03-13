# мое решение
def strStr(haystack: str, needle: str) -> int:
    if needle == '':
        return 0

    for i in range(0, len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


print(strStr(haystack="a", needle="qweqweqweqweq"))
