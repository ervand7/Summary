def convert_to_title(column_number: int) -> str:
    result = ""
    while column_number > 0:
        column_number -= 1
        result = chr(column_number % 26 + 65) + result
        column_number //= 26
    return result


print(convert_to_title(701))