# my solution
def bitwise_complement(n: int) -> int:
    def int_to_bin(num: int) -> str:
        if num == 0:
            return "0"

        result = ""
        while num > 0:
            result += str(num % 2)
            num //= 2

        return result[::-1]

    def bin_to_int(binary_str: str) -> int:
        result = 0
        for i in binary_str:
            result = result * 2 + int(i)
        return result

    binary_str = int_to_bin(n)
    binary_str_inversed = "".join(["0" if i == "1" else "1" for i in binary_str])
    return bin_to_int(binary_str_inversed)


# ChatGPT solution
def bitwise_complement(n: int) -> int:
    if n == 0:
        return 1

    binary = bin(n)[2:]  # get binary string without '0b'
    flipped = ''.join('0' if bit == '1' else '1' for bit in binary)
    return int(flipped, 2)
