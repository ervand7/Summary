# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes
# 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Constraints:
#
# -231 <= x <= 231 - 1
#
#
# Follow up: Could you solve it without converting the integer to a string?

def is_int_palindrome(n: int) -> bool:
    # Check if negative or ends with 0 (except when n is 0)
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    # Reverse half of the number
    reversed_num = 0
    while n > reversed_num:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10

    # If the length of x is odd, we need to remove the middle digit
    return n == reversed_num or n == reversed_num // 10


print(is_int_palindrome(123444321))