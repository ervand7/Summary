from typing import List


# my solution
def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
    h1, h2 = {}, {}
    for i in range(len(list1)):
        h1[list1[i]] = i

    for i in range(len(list2)):
        h2[list2[i]] = i

    result = []
    min_sum = float("inf")
    for k, v in h1.items():
        if k in h2:
            summa = v + h2[k]
            if summa < min_sum:
                min_sum = summa
                result = [k]
            elif summa == min_sum:
                result.append(k)

    return result


# ChatGPT solution
def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
    index_map = {string: index for index, string in enumerate(list1)}
    min_sum = float('inf')
    result = []

    for index, string in enumerate(list2):
        if string in index_map:
            index_sum = index + index_map[string]
            if index_sum < min_sum:
                min_sum = index_sum
                result = [string]
            elif index_sum == min_sum:
                result.append(string)

    return result
