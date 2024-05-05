# def foo(item, lst=[]):
#     lst.append(item)
#     return lst
#
# print(foo(1))
# print(foo(2, []))
# print(foo(3, []))
# print(foo(4))


def add_strings(num1: str, num2: str) -> str:
    pointer1, pointer2 = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while pointer1 >= 0 or pointer2 >= 0 or carry:
        n1 = int(num1[pointer1]) if pointer1 >= 0 else 0
        n2 = int(num2[pointer2]) if pointer2 >= 0 else 0

        total = n1 + n2 + carry
        carry = total // 10
        result.append(str(total % 10))

        pointer1 -= 1
        pointer2 -= 1

    return ''.join(reversed(result))


print(add_strings("9999999", "1"))
