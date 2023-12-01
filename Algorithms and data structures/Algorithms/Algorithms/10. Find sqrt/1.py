# O(log n)
# Классическая задача на алгоритм "Разделяй и властвуй".
# Применяем бинарный поиск для нахождения числа, которое при умножении
# на себя равно n.

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


print(get_sqrt(1234512345))


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


print(get_sqrt_recursive(1234512345))
