def max_repeating(sequence: str, word: str) -> int:
    n, m = len(sequence), len(word)
    dp = [0] * n
    result = 0

    for i in range(n):
        # Only try if the ending window fits
        if i + 1 >= m and sequence[i + 1 - m: i + 1] == word:
            if i >= m:
                dp[i] = dp[i - m] + 1
            else:
                dp[i] = 1
            result = max(result, dp[i])

    return result


print(max_repeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
