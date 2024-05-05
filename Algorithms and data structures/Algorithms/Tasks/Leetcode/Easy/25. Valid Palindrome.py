# my solution
def is_palindrome(c: str) -> bool:
    low = 0
    high = len(c) - 1
    while low < high:
        if c[low].isalnum() and c[high].isalnum():
            if c[low].lower() != c[high].lower():
                return False
            low += 1
            high -= 1

        while c[low].isalnum() is False and low < high:
            low += 1
        while c[high].isalnum() is False and low < high:
            high -= 1

    return True


print(is_palindrome("A man, start plan, start canal: Panama"))
