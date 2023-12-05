# O(log n)
# Классическая задача на алгоритм "Разделяй и властвуй".
# Применяем бинарный поиск для нахождения числа, которое при умножении
# на себя равно n.

# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#
# Example 1:
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the
# nearest integer, 2 is returned.
#
#
# Constraints:
#
# 0 <= x <= 231 - 1

def get_sqrt(n: int) -> int:
    if n == 0:
        return 0

    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid

        if mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1

    return right


print(get_sqrt(12321))


def get_sqrt_recursive(n: int, left: int = 0, right: int = 0) -> int:
    if n == 0:
        return 0

    if left > right:
        return right

    if left == 0 and right == 0:
        left = 1
        right = n
    mid = (left + right) // 2
    if mid * mid == n:
        return mid

    if mid * mid < n:
        return get_sqrt_recursive(n, mid + 1, right)
    return get_sqrt_recursive(n, left, mid - 1)


print(get_sqrt_recursive(12321))
