from typing import List


# my solution
def min_operations(boxes: str) -> List[int]:
    n = len(boxes)
    result = {i: 0 for i in range(n)}

    for i in range(n):
        for j in range(n):
            if j != i and boxes[j] != "0":
                result[i] += abs(j - i)

    return list(result.values())


# ChatGPT solution
def min_operations(boxes: str):
    n = len(boxes)
    answer = [0] * n

    # ---- Left pass ----
    balls = 0  # how many balls we've seen so far from the left
    ops = 0  # total operations needed from the left side

    for i in range(n):
        answer[i] += ops
        balls += boxes[i] == '1'
        ops += balls

    # ---- Right pass ----
    balls = 0  # same idea, but from the right side
    ops = 0

    for i in range(n - 1, -1, -1):
        answer[i] += ops
        balls += boxes[i] == '1'
        ops += balls

    return answer


print(min_operations(boxes="001011"))
