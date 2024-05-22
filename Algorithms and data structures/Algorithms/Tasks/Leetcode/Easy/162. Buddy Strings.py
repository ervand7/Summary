# my solution
def buddy_strings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    if s == goal:
        if len(set(s)) < len(s):
            return True
        else:
            return False

    indexes = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            indexes.append(i)

    if len(indexes) != 2:
        return False

    i, j = indexes
    if s[i] == goal[j] and s[j] == goal[i]:
        return True

    return False
