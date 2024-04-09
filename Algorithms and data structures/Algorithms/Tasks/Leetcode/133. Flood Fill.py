from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    m, n = len(image), len(image[0])
    original_color = image[sr][sc]

    # To avoid repainting the same color
    if original_color == color:
        return image

    def dfs(r, c):
        if image[r][c] == original_color:
            image[r][c] = color
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < m:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < n:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill(image, sr=1, sc=1, color=2))
