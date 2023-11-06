def palindrome(x):
    if len(x) <= 1:
        return True
    if x[0] != x[-1]:
        return False
    return palindrome(x[1:-1])


print(palindrome('qwqqeewq'))  # False
