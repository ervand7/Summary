# my solution
def tribonacci(n: int) -> int:
    if n in {1, 2}:
        return 1

    a, b, c = 0, 1, 1
    result = 0
    for _ in range(2, n):
        result = a + b + c
        a, b, c = b, c, result

    return result
