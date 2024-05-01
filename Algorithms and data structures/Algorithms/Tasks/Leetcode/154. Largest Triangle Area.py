from typing import List


def largest_triangle_area(points: List[List[int]]) -> float:
    # Function to calculate the area of a triangle given its three vertices
    def triangle_area(p1, p2, p3):
        # The vertices are p1, p2, p3 with coordinates (x1, y1), (x2, y2), (x3, y3)
        # We use the determinant formula to compute the area of the triangle
        return abs(p1[0] * (p2[1] - p3[1]) +
                   p2[0] * (p3[1] - p1[1]) +
                   p3[0] * (p1[1] - p2[1])) / 2

    max_area = 0  # Initialize max_area to zero, which will store the largest area found
    num_points = len(points)  # Get the total number of points

    # Iterate over all combinations of three distinct points
    for i in range(num_points):
        for j in range(i + 1, num_points):
            for k in range(j + 1, num_points):
                # Calculate the area of the triangle formed by points[i], points[j], and points[k]
                current_area = triangle_area(points[i], points[j], points[k])
                # Update max_area if the current_area is larger than what we have found before
                max_area = max(max_area, current_area)

    return max_area
