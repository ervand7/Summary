def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    counter = []
    while x:
        item = x % 10
        x //= 10
        counter.append(item)
    if counter == counter[::-1]:
        return True
    return False


print(isPalindrome(-121))