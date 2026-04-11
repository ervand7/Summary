from typing import List


# my solution
def find_different_binary_string(nums: List[str]) -> str:
    n = len(nums[0])

    unique = set(nums)
    for string in nums:
        for i in range(n):
            inverted = "1" if string[i] == "0" else "0"
            attempt = string[:i] + inverted + string[i + 1:]
            if attempt not in unique:
                return attempt


# ChatGPT solution
def find_different_binary_string(nums: List[str]) -> str:
    result = []

    for i in range(len(nums)):
        if nums[i][i] == '0':
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)
