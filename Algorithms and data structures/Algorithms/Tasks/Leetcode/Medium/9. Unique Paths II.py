from typing import List


# ChatGPT solution
def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    m, n = len(obstacle_grid), len(obstacle_grid[0])

    # Edge case: if the start or end point is an obstacle
    if obstacle_grid[0][0] == 1 or obstacle_grid[m - 1][n - 1] == 1:
        return 0

    # Initialize DP table
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1  # Starting point

    # Fill the DP table
    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:
                dp[i][j] = 0  # No paths through obstacles
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]  # Add paths from above
                if j > 0:
                    dp[i][j] += dp[i][j - 1]  # Add paths from left

    # Return the result from the bottom-right corner
    return dp[m - 1][n - 1]


print(unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
