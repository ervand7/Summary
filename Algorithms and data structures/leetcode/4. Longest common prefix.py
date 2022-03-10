# O(n2)
def longestCommonPrefix(strs: List[str]) -> str:
    if not all(strs):
        return ''
    min_elem = min(strs)
    counter = 0
    for i in range(len(min_elem)):
        if len(set([elem[i] for elem in strs])) == 1:
            counter += 1
        else:
            break

    return min_elem[:counter]


# O(n)
def second_solution(strs):
    prefix = []
    for x in zip(*strs):
        if len(set(x)) == 1:
            prefix.append(x[0])
        else:
            break
    return "".join(prefix)


# O(n) интересное решение
def third(strs: List[str]) -> str:
    strs.sort()

    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            return strs[0][:i]

    return strs[0]
