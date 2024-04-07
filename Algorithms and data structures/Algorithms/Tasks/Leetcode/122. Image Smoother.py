from typing import List


def image_smoother(img: List[List[int]]) -> List[List[int]]:
    # Dimensions of the image
    m, n = len(img), len(img[0])
    # Initialize the result matrix with zeros
    res = [[0 for _ in range(n)] for _ in range(m)]

    # Directions to navigate through the neighbors
    directions = [(0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]

    for i in range(m):
        for j in range(n):
            sum_val, count = 0, 0
            for dir in directions:
                new_i, new_j = i + dir[0], j + dir[1]
                # Check if the neighbor is within the bounds
                if 0 <= new_i < m and 0 <= new_j < n:
                    sum_val += img[new_i][new_j]
                    count += 1

            # Calculate the average and update the result matrix
            res[i][j] = sum_val // count

    return res
