from typing import List


# my solution
def generate(num_rows: int) -> List[List[int]]:
    if num_rows == 0:
        return []

    if num_rows == 1:
        return [[1]]

    result = [[1], [1, 1]]
    for _ in range(2, num_rows):
        prev = result[-1]
        item = [1]
        for i in range(1, len(prev)):
            item.append(prev[i - 1] + prev[i])
        item.append(1)
        result.append(item)

    return result


print(generate(10))
