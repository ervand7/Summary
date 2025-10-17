# my solution
def int_to_roman(num: int) -> str:
    first = second = third = fourth = ""
    if num >= 1000:
        first = "M" * (num // 1000)

    if num >= 100:
        n = num // 100 % 10
        if n in {1, 2, 3}:
            second = n * "C"
        elif n == 4:
            second = "CD"
        elif n == 5:
            second = "D"
        elif n in {6, 7, 8}:
            second = "D" + "C" * (n % 5)
        elif n == 9:
            second = "CM"

    if num >= 10:
        n = num // 10 % 10
        if n in {1, 2, 3}:
            third = n * "X"
        elif n == 4:
            third = "XL"
        elif n == 5:
            third = "L"
        elif n in {6, 7, 8}:
            third = "L" + "X" * (n % 5)
        elif n == 9:
            third = "XC"

    if num >= 1:
        n = num % 10
        if n in {1, 2, 3}:
            fourth = n * "I"
        elif n == 4:
            fourth = "IV"
        elif n == 5:
            fourth = "V"
        elif n in {6, 7, 8}:
            fourth = "V" + "I" * (n % 5)
        elif n == 9:
            fourth = "IX"

    return first + second + third + fourth


# ChatGPT solution
def int_to_roman(num: int) -> str:
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    result = []
    for value, symbol in zip(values, symbols):
        while num >= value:
            num -= value
            result.append(symbol)

    return ''.join(result)


print(int_to_roman(3749))
