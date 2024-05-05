from typing import List


# my solution
def is_one_bit_character(bits: List[int]) -> bool:
    pointer = 0
    while pointer < len(bits):
        if pointer == len(bits) - 1 and bits[pointer] == 0:
            return True

        if bits[pointer] == 0:
            pointer += 1
        else:
            pointer += 2

    return False
