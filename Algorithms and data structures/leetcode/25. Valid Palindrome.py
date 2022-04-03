def isPalindrome(string: str) -> bool:
    start = 0
    end = len(string) - 1
    while start < end:
        while start < end and not string[start].isalnum():
            start += 1
        while start < end and not string[end].isalnum():
            end -= 1
        if string[start].lower() != string[end].lower():
            return False
        start += 1
        end -= 1
    return True


print(isPalindrome("A man, start plan, start canal: Panama"))
