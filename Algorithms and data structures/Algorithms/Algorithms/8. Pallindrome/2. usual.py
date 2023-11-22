def is_palindrome(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True


print(is_palindrome('asdfghjjhgfdsa'))  # True
