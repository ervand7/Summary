def convert_to_base7(num: int) -> str:
    if num == 0:
        return "0"

    negative = num < 0
    num = abs(num)
    result = ""
    while num:
        result = str(num % 7) + result
        num //= 7
    return "-" + result if negative else result


print(convert_to_base7(100))
