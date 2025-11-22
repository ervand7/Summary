from typing import List


# my solution
def pivot_array(nums: List[int], pivot: int) -> List[int]:
    lt, eq, gt = [], [], []
    for i in nums:
        if i < pivot:
            lt.append(i)
        elif i == pivot:
            eq.append(i)
        else:
            gt.append(i)

    return lt + eq + gt
