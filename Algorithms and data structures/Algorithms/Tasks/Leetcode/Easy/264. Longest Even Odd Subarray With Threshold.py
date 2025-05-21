from typing import List


# my solution
def longest_alternating_subarray(nums: List[int], threshold: int) -> int:
    def find_new_start(start: int) -> int:
        while start < n:
            if nums[start] % 2 == 0:
                break
            start += 1

        return start

    n = len(nums)
    start = 0
    result = 0

    first = True
    while start < (n):
        if nums[start] > threshold or nums[start] % 2 != 0:
            if start == n - 1:
                break
            if nums[start] % 2 == 0:
                start = find_new_start(start + 1)
            else:
                start = find_new_start(start)
            continue

        if first:
            result += 1
            first = False

        current_should_be_even = False

        for j in range(start + 1, n):
            if nums[j] > threshold:
                break
            if (nums[j] % 2 == 0) == current_should_be_even:
                current_should_be_even = not current_should_be_even
            else:
                break

            result = max(result, j - start + 1)

        start = start + 1

    return result


# ChatGPT solution
def longest_alternating_subarray(nums: List[int], threshold: int) -> int:
    max_len = cur_len = 0  # best and current streak lengths
    prev_parity = None  # parity of previous element in streak

    for x in nums:
        # rule 3 – every value must be ≤ threshold
        if x > threshold:
            cur_len = 0
            prev_parity = None
            continue

        if cur_len == 0:
            # we are not inside a streak – can we start one here?
            if x % 2 == 0:  # rule 1 – first number must be even
                cur_len = 1
                prev_parity = 0
            # else: odd → cannot start, leave cur_len = 0
        else:
            # we are inside a streak – can we extend it?
            if x % 2 != prev_parity:  # rule 2 – must alternate parity
                cur_len += 1
                prev_parity ^= 1  # flip 0↔1
            else:
                # parity repeated → current streak ends
                if x % 2 == 0:  # but if x is even we can start anew here
                    cur_len = 1
                    prev_parity = 0
                else:  # odd cannot start a new streak
                    cur_len = 0
                    prev_parity = None

        max_len = max(max_len, cur_len)

    return max_len


print(longest_alternating_subarray(nums=[2, 3, 3, 10], threshold=10))
