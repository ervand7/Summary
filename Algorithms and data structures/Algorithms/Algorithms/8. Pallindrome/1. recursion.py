def is_palindrome(x):
    if len(x) <= 1:
        return True
    if x[0] != x[-1]:
        return False
    return is_palindrome(x[1:-1])


print(is_palindrome('asdfghjjhgfdsa'))  # True
