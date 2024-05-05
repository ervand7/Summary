from typing import List


# my solution
def count_bits(n: int) -> List[int]:
    result = []
    for i in range(n + 1):
        val = str(bin(i))
        val = val.split("b")[1]
        val = sum([int(i) for i in val])
        result.append(val)

    return result


# ChatGPT solution
def count_bits(n: int) -> List[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans
