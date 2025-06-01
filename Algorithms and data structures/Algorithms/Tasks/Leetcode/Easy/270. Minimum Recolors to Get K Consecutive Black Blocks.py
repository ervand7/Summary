def minimum_recolors(blocks: str, k: int) -> int:
    n = len(blocks)
    h = {}
    result = float('inf')

    for i in range(n - k + 1):
        if i == 0:
            for item in range(k):
                h[blocks[item]] = h.get(blocks[item], 0) + 1

        else:
            h[blocks[i - 1]] -= 1
            h[blocks[i + k - 1]] = h.get(blocks[i + k - 1], 0) + 1

        result = min(result, h.get("W", 0))

    return result


print(minimum_recolors(blocks="WBBWWBBWBW", k=7))


# ChatGPT solution
def minimum_recolors(blocks: str, k: int) -> int:
    current_white = 0

    # First window
    for i in range(k):
        if blocks[i] == 'W':
            current_white += 1
    min_ops = current_white

    # Slide the window
    for i in range(k, len(blocks)):
        if blocks[i - k] == 'W':
            current_white -= 1
        if blocks[i] == 'W':
            current_white += 1
        min_ops = min(min_ops, current_white)

    return min_ops


print(minimum_recolors(blocks="WBBWWBBWBW", k=7))
