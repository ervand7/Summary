def to_hex(num: int) -> str:
    if num == 0:
        return "0"
    elif num < 0:
        # For negative numbers, calculate two's complement
        num += 2**32

    hex_chars = "0123456789abcdef"
    hex_str = ""

    while num > 0:
        idx = num % 16
        char = hex_chars[idx]
        hex_str = char + hex_str
        num //= 16

    return hex_str


print(to_hex(123))