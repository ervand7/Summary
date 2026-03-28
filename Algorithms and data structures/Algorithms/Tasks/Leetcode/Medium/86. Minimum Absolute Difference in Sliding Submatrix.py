from typing import List

a = [
    [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
    [5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8],
    [9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12],
    [13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16]
]


# my brute-force solution
# Time:  O(m * n * k^2 * log k)
# Space: O(m * n)
def min_abs_diff(grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    minimums = []

    for i in range(m):
        for j in range(n):
            if (i + k <= m) and (j + k <= n):
                values = []
                for row in range(i, i + k):
                    values.extend(grid[row][j:j + k])

                if len(values) == 1:
                    minimums.append(0)
                    continue

                values = list(set(values))
                values.sort(reverse=True)
                min_diff = float("inf")
                for idx in range(len(values) - 1):
                    min_diff = min(min_diff, values[idx] - values[idx + 1])

                if min_diff == float("inf"):
                    min_diff = 0
                minimums.append(min_diff)

    # form result
    result = []
    result_m = m - k + 1
    result_n = n - k + 1
    i = 0
    for _ in range(result_m):
        row = []
        for _ in range(result_n):
            row.append(minimums[i])
            i += 1

        result.append(row)

    return result


# ChatGPT solution
# Time:  O(m * n * k^2 * log k)
# Space: O(m * n)
def min_abs_diff(grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

    for i in range(m - k + 1):
        for j in range(n - k + 1):
            values = set()

            # collect all values in the current k x k submatrix
            for r in range(i, i + k):
                for c in range(j, j + k):
                    values.add(grid[r][c])

            # if all elements are the same, answer is 0
            if len(values) <= 1:
                ans[i][j] = 0
                continue

            sorted_vals = sorted(values)

            best = float("inf")
            for t in range(1, len(sorted_vals)):
                best = min(best, sorted_vals[t] - sorted_vals[t - 1])

            ans[i][j] = best

    return ans
