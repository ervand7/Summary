def is_int_palindrome(n: int) -> bool:
    temp = []
    while n:
        item = n % 10
        n //= 10
        temp.append(item)

    for i in range(len(temp) // 2):
        if temp[i] != temp[len(temp) - 1 - i]:
            return False
    return True


print(is_int_palindrome(123444321))