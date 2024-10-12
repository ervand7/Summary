from typing import List


# my solution
# O(n + m), where n is the number of people and m is the number of trust relationships
def find_judge(n: int, trust: List[List[int]]) -> int:
    if not trust:
        return n if n == 1 else -1

    unique = set()
    h = {}
    for first, second in trust:
        unique.add(first)
        unique.add(second)

        exists = h.get(first, False)
        if exists:
            h[first].add(second)
        else:
            h[first] = {second}

    judge = 0
    judges_count = 0
    for i in unique:
        if i not in h:
            judge = i
            judges_count += 1

    if judges_count > 1:
        return -1

    for k, v in h.items():
        if judge not in v:
            return -1

    return judge


# ChatCPT solution
# O(n + m), where n is the number of people and m is the number of trust relationships
def find_judge(n, trust):
    if n == 1 and not trust:
        return 1

    trust_scores = [0] * (n + 1)

    for a, b in trust:
        trust_scores[a] -= 1
        trust_scores[b] += 1

    for i in range(1, n + 1):
        if trust_scores[i] == n - 1:
            return i

    return -1


find_judge(n=3, trust=[[1, 3], [2, 3]])
