def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    start = 1
    end = x // 2
    while start <= end:
        mid = (start + end) // 2
        sqr = mid * mid
        if sqr == x:
            return mid
        if sqr <= x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


print(mySqrt(12345))
