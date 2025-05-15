from typing import List


# my solution
def can_form_array(arr: List[int], pieces: List[List[int]]) -> bool:
    h = {}
    for i in range(len(arr)):
        h[arr[i]] = i

    values = []
    for i in pieces:
        if len(i) == 1:
            values.append(i[0])
        else:
            start_idx = h.get(i[0], None)
            if start_idx is not None:
                if arr[start_idx:start_idx + len(i)] == i:
                    values.extend(i)

    return set(arr) == set(values)


print(can_form_array(arr=[1, 2, 3, 4], pieces=[[2, 3], [1], [4]]))
