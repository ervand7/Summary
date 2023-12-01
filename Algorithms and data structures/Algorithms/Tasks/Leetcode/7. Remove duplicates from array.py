from typing import List


def removeDuplicates(nums: List[int]) -> int:
    left = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[left] = nums[i]
            left += 1
    return left


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# --------------------------------------------------------
# my
def remove_duplicates(arr: list) -> None:
    hash_table = {}
    for i in range(len(arr)):
        hash_table[arr[i]] = True
    for idx, key in enumerate(hash_table.keys()):
        arr[idx] = key
    for i in range(len(arr), len(hash_table), -1):
        arr.pop()


a = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 5, 5, 4, 3, 2, 1]
print(hex(id(a)))  # 0x7fdf78283940
remove_duplicates(a)
print(a)
print(hex(id(a)))  # 0x7fdf78283940
