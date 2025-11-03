from typing import List


# my solution
def generate(num_rows: int) -> List[List[int]]:
    if num_rows == 1:
        return [[1]]

    result = [[1], [1, 1]]
    if num_rows == 2:
        return result

    for i in range(1, num_rows - 1):
        item = []
        prev = result[i]
        for j in range(1, len(prev)):
            item.append(prev[j - 1] + prev[j])

        item = [1] + item + [1]

        result.append(item)

    return result


# ChatGPT solution
def generate(num_rows: int) -> List[List[int]]:
    triangle = [[1] * (i + 1) for i in range(num_rows)]
    for i in range(2, num_rows):
        prev = triangle[i - 1]
        curr = triangle[i]
        for j in range(1, i):
            curr[j] = prev[j - 1] + prev[j]
    return triangle


print(generate(2))
