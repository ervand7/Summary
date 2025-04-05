def int_to_bin(num):
    if num == 0:
        return "0"
    binary = []
    while num > 0:
        # Append the remainder (0 or 1) to the binary list
        binary.append(str(num % 2))
        # Divide the number by 2
        num = num // 2
    # Reverse the list and join to get the binary representation
    return ''.join(reversed(binary))


print(int_to_bin(77))


def bin_to_int(binary_str):
    result = 0
    for digit in binary_str:
        result = result * 2 + int(digit)
    return result


print(bin_to_int("011010101011111"))