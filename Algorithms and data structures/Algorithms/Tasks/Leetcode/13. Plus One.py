from typing import List


def plusOne(digits: List[int]) -> List[int]:
    converted = int(''.join([str(i) for i in digits]))
    result = converted + 1
    result = [int(i) for i in str(result)]
    return result
