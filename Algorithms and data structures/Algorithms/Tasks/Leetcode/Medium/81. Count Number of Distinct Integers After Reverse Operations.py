from typing import List


def count_distinct_integers(nums: List[int]) -> int:
    def reverse_num(n: int) -> int:
        rev = 0
        while n:
            rev = rev * 10 + n % 10
            n //= 10
        return rev

    nums_set = set(nums)

    for n in nums:
        nums_set.add(reverse_num(n))

    return len(nums_set)


print(count_distinct_integers(nums=[1, 13, 10, 12, 31]))
