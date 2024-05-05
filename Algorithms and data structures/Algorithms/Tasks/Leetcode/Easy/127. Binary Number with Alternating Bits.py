# my solution
def has_alternating_bits(n: int) -> bool:
    def int_to_bin(num):
        if num == 0:
            return "0"
        binary = []
        while num > 0:
            binary.append(str(num % 2))
            num = num // 2
        return ''.join(reversed(binary))

    s = int_to_bin(n)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False

    return True
