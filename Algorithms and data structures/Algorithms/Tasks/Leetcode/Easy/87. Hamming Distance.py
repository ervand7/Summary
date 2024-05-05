# my solution
def hamming_distance(x: int, y: int) -> int:
    def int_to_bin_array(n: int):
        if n == 0:
            return [0]

        result = []
        while n:
            result.append(n % 2)
            n //= 2

        return result[-1::-1]

    first = int_to_bin_array(x)
    second = int_to_bin_array(y)

    if len(first) > len(second):
        diff_count = len(first) - len(second)
        second = [0] * diff_count + second
    else:
        diff_count = len(second) - len(first)
        first = [0] * diff_count + first

    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1

    return count


print(hamming_distance(123, 345))  # 3


# ChatGPT solution
def hamming_distance(x: int, y: int) -> int:
    # XOR of x and y gives a number with 1s where bits differ
    xor = x ^ y
    # Count the number of 1s in the binary representation of xor
    return bin(xor).count('1')


print(hamming_distance(123, 345))  # 3
