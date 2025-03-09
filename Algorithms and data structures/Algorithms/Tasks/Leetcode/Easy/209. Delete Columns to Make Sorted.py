from typing import List


# my solution
def min_deletion_size(strs: List[str]) -> int:
    columns_ignore = set()
    n = len(strs)
    m = len(strs[0])
    result = 0

    for i in range(1, n):
        for j in range(m):
            if len(columns_ignore) == m:
                return result
            if j in columns_ignore:
                continue
            if strs[i][j] < strs[i - 1][j]:
                columns_ignore.add(j)
                result += 1

    return result


# ChatGPT better solution
def min_deletion_size(strs: List[str]) -> int:
    if not strs:
        return 0

    num_rows = len(strs)
    num_cols = len(strs[0])
    delete_count = 0

    # Iterate over each column.
    for j in range(num_cols):
        # Check each adjacent pair in the column.
        for i in range(num_rows - 1):
            if strs[i][j] > strs[i + 1][j]:
                delete_count += 1
                break  # No need to check further in this column.
    return delete_count
