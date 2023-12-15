from collections import defaultdict


def contains_nearby_duplicate(nums, k):
    hash_table = {}
    for idx, v in enumerate(nums):
        if v in hash_table and idx - hash_table[v] <= k:
            return True
        hash_table[v] = idx

    return False


print(contains_nearby_duplicate([1, 2, 3, 1], 3))


# my solution
def contains_nearby_duplicate(nums, k):
    hash_table = defaultdict(list)
    for i in range(len(nums)):
        hash_table[nums[i]].append(i)

    for _, value in hash_table.items():
        if len(value) > 1:
            for i in range(1, len(value)):
                if abs(value[i - 1] - value[i]) <= k:
                    return True

    return False


print(contains_nearby_duplicate([1, 2, 3, 1], 3))
