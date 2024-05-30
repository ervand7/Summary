from typing import List


# my solution (not fast, not for large cases)
def fair_candy_swap(alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
    alice_sum = sum(alice_sizes)
    bob_sum = sum(bob_sizes)
    for i in set(alice_sizes):
        for j in bob_sizes:
            if (alice_sum - i + j) == (bob_sum - j + i):
                return [i, j]


# CgatGPT solution
def fair_candy_swap(alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
    sum_alice = sum(alice_sizes)
    sum_bob = sum(bob_sizes)
    diff = (sum_bob - sum_alice) // 2  # This is the amount that Bob has more than Alice divided by 2

    # Create a set for Bob's candy sizes for quick lookup
    bob_set = set(bob_sizes)

    for x in alice_sizes:
        y = x + diff  # Find the corresponding y that Bob should give in exchange for x
        if y in bob_set:
            return [x, y]


print(fair_candy_swap([1, 3], [2]))
