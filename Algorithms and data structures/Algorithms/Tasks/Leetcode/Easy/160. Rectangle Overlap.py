from typing import List


def is_rectangle_overlap(rec1: List[int], rec2: List[int]) -> bool:
    # Check if rec1 is to the left of rec2
    if rec1[2] <= rec2[0]:
        return False
    # Check if rec1 is to the right of rec2
    if rec1[0] >= rec2[2]:
        return False
    # Check if rec1 is above rec2
    if rec1[1] >= rec2[3]:
        return False
    # Check if rec1 is below rec2
    if rec1[3] <= rec2[1]:
        return False
    # If none of the above conditions are true, the rectangles overlap
    return True
