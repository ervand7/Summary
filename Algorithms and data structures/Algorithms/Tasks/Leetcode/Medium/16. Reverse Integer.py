# my solution
def reverse(x: int) -> int:
    if x == 0:
        return x

    is_positive = x > 0
    x_list = list(str(x)) if is_positive else list(str(x)[1:])
    len_x_list = len(x_list)
    for i in range(len_x_list // 2):
        x_list[i], x_list[len_x_list - 1 - i] = x_list[len_x_list - 1 - i], x_list[i]

    while x_list[0] == 0:
        x_list = x_list[1:]

    x_converted = int("".join(x_list)) if is_positive else -int("".join(x_list))
    if -2 ** 31 <= x_converted <= 2 ** 31 - 1:
        return x_converted
    return 0


# GhatGPT solution
def reverse(x: int) -> int:
    minimum, maximum = -2 ** 31, 2 ** 31 - 1
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        digit = x % 10
        x //= 10

        result = result * 10 + digit
        if not minimum <= result <= maximum:
            return 0

    return sign * result
