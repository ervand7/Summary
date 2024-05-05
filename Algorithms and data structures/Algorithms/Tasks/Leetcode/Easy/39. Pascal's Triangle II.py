from typing import List


# my solution
def get_row(row_index: int) -> List[int]:
    if row_index == 0:
        return [1]

    result = [[1], [1, 1]]
    for _ in range(1, row_index):
        prev = result[-1]
        item = [1]
        for i in range(1, len(prev)):
            item.append(prev[i - 1] + prev[i])
        item.append(1)
        result.append(item)

    return result[-1]
