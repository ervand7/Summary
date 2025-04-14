from typing import List


# my solution
def min_time_to_visit_all_points(points: List[List[int]]) -> int:
    count = 0
    start = points[0]
    for p in points[1:]:
        x, y = start
        x_target, y_target = p
        while x != x_target and y != y_target:
            if x < x_target:
                x += 1
            else:
                x -= 1

            if y < y_target:
                y += 1
            else:
                y -= 1

            count += 1

        if x != x_target:
            count += abs(x - x_target)
        elif y != y_target:
            count += abs(y - y_target)

        start = [x_target, y_target]

    return count


print(min_time_to_visit_all_points([[3, 2], [-2, 2]]))


# ChatGPT solution
def min_time_to_visit_all_points(points: List[List[int]]) -> int:
    time = 0
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        time += max(abs(x2 - x1), abs(y2 - y1))
    return time
