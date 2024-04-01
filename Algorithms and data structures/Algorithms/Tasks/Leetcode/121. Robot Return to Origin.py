# my solution
def judge_circle(moves: str) -> bool:
    h = {}
    for i in moves:
        h[i] = h.get(i, 0) + 1

    return h.get("U", 0) == h.get("D", 0) and h.get("L", 0) == h.get("R", 0)


# ChatGPT solution
def judge_circle(moves: str) -> bool:
    # Starting position
    x, y = 0, 0

    # Apply each move to the robot's position
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1

    # Check if the robot returns to the origin
    return x == 0 and y == 0
