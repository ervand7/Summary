from typing import List


def surface_area(grid: List[List[int]]) -> int:
    n = len(grid)

    total_area = 0
    for i in range(n):
        for j in range(n):
            # If there are cubes in the current cell
            if grid[i][j] > 0:
                # Add surface area for top and bottom faces
                total_area += 2  # Top and bottom

                # Add surface area for the four vertical faces
                # Each cube has 4 vertical faces, multiply by the number of cubes
                total_area += grid[i][j] * 4

                # Subtract the hidden faces between current cell and the cell to the left
                if i > 0:
                    total_area -= min(grid[i][j], grid[i - 1][j]) * 2

                # Subtract the hidden faces between current cell and the cell above
                if j > 0:
                    total_area -= min(grid[i][j], grid[i][j - 1]) * 2

    return total_area
