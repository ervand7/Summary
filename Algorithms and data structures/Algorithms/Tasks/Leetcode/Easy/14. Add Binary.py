# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010",
#        b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


print(add_binary(a="10001010101", b="1111"))


def add_binary(a: str, b: str) -> str:
    result = []
    carry = 0

    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        current_sum = digit_a + digit_b + carry
        carry = current_sum // 2
        current_sum %= 2

        result.insert(0, str(current_sum))

        i -= 1
        j -= 1

    return ''.join(result)


print(add_binary(a="10001010101", b="1111"))

