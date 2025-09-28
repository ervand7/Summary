from typing import List


def num_identical_pairs(nums: List[int]) -> int:
    def get_all_possible_pairs_combinations_count(elems_count: int) -> int:
        return elems_count * (elems_count - 1) // 2

    h = {}
    for i in nums:
        h[i] = h.get(i, 0) + 1

    result = 0

    for v in h.values():
        result += get_all_possible_pairs_combinations_count(v)
    return result
