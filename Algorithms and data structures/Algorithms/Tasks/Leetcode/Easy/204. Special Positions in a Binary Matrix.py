from typing import List


# my solution
def num_special(mat: List[List[int]]) -> int:
    result = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                if sum(mat[i]) == 1 and sum([mat[row][j] for row in range(len(mat))]) == 1:
                    result += 1
                    break

    return result
