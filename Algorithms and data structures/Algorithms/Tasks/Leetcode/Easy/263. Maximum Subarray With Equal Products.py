from typing import List


# my solution
def max_length(nums: List[int]) -> int:
    def product(nums: List[int]) -> int:
        result = 1
        for i in nums:
            result *= i

        return result

    def gcd(nums: List[int]) -> int:
        values = list(set(nums))
        values.sort()
        result = 1
        attempt = result + 1
        while attempt <= values[0]:
            is_common_divisor_for_all = True
            for i in values:
                if i % attempt != 0:
                    is_common_divisor_for_all = False
                    break

            if is_common_divisor_for_all is True:
                result = attempt

            attempt += 1

        return result

    def lcm(nums: List[int]) -> int:
        max_value = max(nums)
        attempt = max_value
        while True:
            found = True
            for i in nums:
                if attempt % i != 0:
                    found = False
                    break

            if found is True:
                return attempt
            attempt += max_value

    n = len(nums)
    result = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = nums[i:j]
            p = product(sub)
            g = gcd(sub)
            l = lcm(sub)
            if p == g * l:
                result = max(result, len(sub))

    return result


# ChatGPT solution
def max_length(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    n = len(nums)
    max_len = 0

    for i in range(n):
        prod = 1
        sub_gcd = nums[i]
        sub_lcm = nums[i]

        for j in range(i, n):
            prod *= nums[j]
            sub_gcd = gcd(sub_gcd, nums[j])
            sub_lcm = lcm(sub_lcm, nums[j])

            if prod == sub_gcd * sub_lcm:
                max_len = max(max_len, j - i + 1)

    return max_len


print(max_length([1, 2, 1, 2, 1, 1, 1]))
