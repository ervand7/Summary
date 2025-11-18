def partition(s: str):
    n = len(s)

    # === DP: precompute all palindromic substrings ===
    # is_pal[i][j] will be True if s[i:j+1] is a palindrome
    is_pal = [[False] * n for _ in range(n)]

    # Fill DP table bottom-up:
    # i goes backwards to ensure is_pal[i+1][j-1] is already known
    for i in range(n - 1, -1, -1):
        for j in range(i, n):

            # s[i] == s[j] → boundaries match
            # (j - i <= 2) → substring length 1 or 2, always easy to check
            # or is_pal[i+1][j-1] → middle substring is a palindrome
            if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True  # mark substring as palindrome

    # === Backtracking to build all partitions ===
    result = []  # final list of all palindrome partitions
    path = []  # current combination of substrings

    # Try to partition starting from index `start`
    def backtrack(start):
        # If we consumed all characters — we found a valid partition
        if start == n:
            result.append(path.copy())  # add a copy of current path
            return

        # Try all possible end positions for the next substring
        for end in range(start, n):

            # Only continue if s[start:end+1] is a palindrome
            if is_pal[start][end]:
                path.append(s[start:end + 1])  # choose substring
                backtrack(end + 1)  # explore further
                path.pop()  # undo choice (backtrack)

    # Start building partitions from index 0
    backtrack(0)
    return result


print(partition(s="aab"))
