# O(n)
# нужно из списка найти индексы чисел, сумма которых равна target


from typing import List


def find_summand_indexes(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        summand = target - nums[i]
        if summand in hashmap:
            return [hashmap[summand], i]
        hashmap[nums[i]] = i


print(find_summand_indexes([2, 11, 7, 15], 9))  # [0, 2]
