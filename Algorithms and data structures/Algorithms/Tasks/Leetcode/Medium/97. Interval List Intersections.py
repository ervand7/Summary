from typing import List


# my solution (exceeds time limit)
def interval_intersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i = 0
    j = 0
    result = []

    step = 0
    start, end = 0, 0
    intersects = False
    while i < len(firstList) and j < len(secondList):
        if firstList[i][0] <= step <= firstList[i][1] and secondList[j][0] <= step <= secondList[j][1]:
            if not intersects:
                intersects = True
                start = step

            end = step

        finish_intersection = False
        if step == firstList[i][1]:
            i += 1
            finish_intersection = True
        if step == secondList[j][1]:
            j += 1
            finish_intersection = True

        if intersects and finish_intersection:
            result.append([start, end])
            start, end = 0, 0
            intersects = False

        step += 1

    return result


def interval_intersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i = 0
    j = 0
    res = []

    while i < len(firstList) and j < len(secondList):
        a_start, a_end = firstList[i]
        b_start, b_end = secondList[j]

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        if start <= end:
            res.append([start, end])

        if a_end < b_end:
            i += 1
        else:
            j += 1

    return res


print(interval_intersection(
    firstList=[[8, 15]],
    secondList=[[2, 6], [8, 10], [12, 20]],
))
