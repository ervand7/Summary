def fact1(x):
    if x == 1:
        return x
    return fact1(x - 1) * x


print(fact1(7))


def fact2(x):
    if x == 1:
        return x
    val = fact2(x - 1)
    result = val * x
    return result


print(fact2(7))


def fact3(n: int, result=1):
    if n == 1:
        return result
    return fact3(n - 1, result * n)


print(fact3(7))
