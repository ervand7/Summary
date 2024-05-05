from typing import List


# my solution
def self_dividing_numbers(left: int, right: int) -> List[int]:
    result = []

    for i in range(left, right + 1):
        if i % 10 == 0:
            continue

        val = i
        flag = True

        while val:
            last = val % 10
            if last == 0:
                flag = False
                break

            if i % last != 0:
                flag = False
                break
            val //= 10

        if flag == True:
            result.append(i)

    return result


# ChatGPT solution
def self_dividing_numbers(left, right):
    def is_self_dividing(number):
        for digit in str(number):
            if digit == '0' or number % int(digit) != 0:
                return False
        return True

    return [number for number in range(left, right + 1) if is_self_dividing(number)]
