from typing import List


def count_max_or_subsets(nums: List[int]) -> int:
    # ---- Step 1: Convert each number into a set of bit positions that are 1 ----
    #
    # Example:
    #   5  → binary "101" → bits {0, 2}
    #   6  → binary "110" → bits {1, 2}
    #
    def number_to_bitset(x):
        bits = set()
        position = 0
        while x > 0:
            if x % 2 == 1:  # if the last binary digit is 1
                bits.add(position)  # remember this bit index
            x //= 2
            position += 1
        return bits

    bitsets = [number_to_bitset(x) for x in nums]

    # ---- Step 2: The maximum OR = union of all bits from all numbers ----
    max_or_bits = set()
    for b in bitsets:
        max_or_bits |= b  # set union = OR

    # ---- Step 3: Try all subsets and count which ones give the same OR ----
    n = len(nums)
    count = 0

    # there are 2^n subsets; we skip mask=0 because it's empty
    for mask in range(1, 1 << n):
        current_bits = set()

        # check which elements belong to this subset
        for i in range(n):
            # Check if the i-th element is chosen in this subset
            # Using math instead of bitwise AND:
            if (mask // (2 ** i)) % 2 == 1:
                current_bits |= bitsets[i]  # union = OR

        # If this subset OR equals maximum OR → count it
        if current_bits == max_or_bits:
            count += 1

    return count


print(count_max_or_subsets(nums=[3, 2, 1, 5]))
