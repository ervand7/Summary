def fact1(x):
    if x == 1:
        return x
    val = fact1(x - 1)
    result = val * x
    return result


print(fact1(7))
