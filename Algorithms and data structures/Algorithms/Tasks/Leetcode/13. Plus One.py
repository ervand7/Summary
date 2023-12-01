from typing import List


def plus_one(digits: List[int]) -> List[int]:
    converted = int(''.join([str(i) for i in digits]))
    result = converted + 1
    result = [int(i) for i in str(result)]
    return result


print(plus_one([1, 2, 3, 4]))