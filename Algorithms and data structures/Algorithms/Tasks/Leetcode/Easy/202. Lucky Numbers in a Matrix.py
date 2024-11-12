from typing import List


# my solution O(m * n + m2)
def lucky_numbers(matrix: List[List[int]]) -> List[int]:
    len_matrix = len(matrix)
    for row_idx, row in enumerate(matrix):
        minimum_val, minimum_idx = float("inf"), 0
        for i in range(len(row)):
            if row[i] < minimum_val:
                minimum_val = row[i]
                minimum_idx = i

        maximum_val = max([matrix[i][minimum_idx] for i in range(len_matrix)])
        if maximum_val == minimum_val:
            return [minimum_val]

    return []


# ChatGPT solution
def lucky_numbers(matrix):
    # Step 1: Find the minimum in each row
    row_mins = {min(row) for row in matrix}

    # Step 2: Find the maximum in each column
    col_maxes = {max(col) for col in zip(*matrix)}

    # Step 3: Find the intersection of row mins and column maxes
    lucky_numbers = row_mins & col_maxes

    # Convert the result to a list to match the expected output format
    return list(lucky_numbers)
