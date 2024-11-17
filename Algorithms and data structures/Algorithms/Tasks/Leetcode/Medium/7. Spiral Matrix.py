from typing import List


# my solution
def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []

    def rec(data: List[List[int]]):
        if len(data) == 1:
            result.extend(data[0])
            return

        if all([len(i) == 1 for i in data]):
            for i in data:
                result.extend(i)
            return result

        result.extend(data[0])  # take all first row
        right_side_values = []
        left_side_values = []
        for i in range(1, len(data) - 1):
            right_side_values.append(data[i][-1])
            left_side_values.append(data[i][0])
        result.extend(right_side_values)  # take all right side values
        result.extend(data[-1][::-1])  # take all reversed last row
        result.extend(left_side_values[::-1])  # take all left side values

        # handle nested level
        new_data = [row[1:- 1] for row in data[1:- 1]]
        if not any(new_data):
            return
        rec(new_data)

    rec(matrix)
    return result
