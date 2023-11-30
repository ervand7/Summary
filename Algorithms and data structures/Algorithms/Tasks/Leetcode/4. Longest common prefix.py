from typing import List


# O(n)
def find_longest_common_prefix(strs: List[str]) -> str:
    if len(strs) != 2 or not all(strs):
        return ""

    smallest = min(strs)
    counter = 0
    for i in range(len(smallest)):
        if strs[0][i] == strs[1][i]:
            counter += 1
        else:
            break

    return smallest[:counter]


print(find_longest_common_prefix(["hello", "hello1"]))
