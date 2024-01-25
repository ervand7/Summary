def is_perfect_square(num: int) -> bool:
    left = 1
    right = num

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True

        if mid * mid > num:
            right = mid - 1
        else:
            left = mid + 1

    return False
