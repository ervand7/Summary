# my solution
def count_k_constraint_substrings(s: str, k: int) -> int:
    n = len(s)
    result = 0

    for i in range(n):
        count_0 = count_1 = 0
        for j in range(i, n):
            if s[j] == "0":
                count_0 += 1
            else:
                count_1 += 1
            if count_0 <= k or count_1 <= k:
                result += 1
            else:
                break

    return result
