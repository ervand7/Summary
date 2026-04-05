from typing import List


# my solution
# Time: O(n · k)
# n = number of elements
# k = number of bits
# Space: O(n · k)
def largest_combination(candidates: List[int]) -> int:
    def int_to_bin(num: int) -> str:
        if num == 0:
            return "0"
        binary = []
        while num > 0:
            binary.append(str(num % 2))
            num = num // 2
        return ''.join(reversed(binary))

    max_len = 0
    bins = []
    for i in candidates:
        i_bin = int_to_bin(i)
        bins.append(i_bin)
        max_len = max(max_len, len(i_bin))

    for i in range(len(bins)):
        bins[i] = "0" * (max_len - len(bins[i])) + bins[i]

    result = 0
    for i in range(max_len):
        result = max(result, [row[i] for row in bins].count("1"))

    return result


# ChatGPT solution
# Time: O(n)
# Space: O(1)
def largest_combination(candidates: List[int]) -> int:
    result = 0

    for bit in range(32):
        count = 0
        for num in candidates:
            if num & (1 << bit):
                count += 1
        result = max(result, count)

    return result


print(largest_combination([16, 17, 71, 62, 12, 24, 14]))
