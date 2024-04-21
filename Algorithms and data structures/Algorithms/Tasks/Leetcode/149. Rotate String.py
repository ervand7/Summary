# my solution
def rotate_string(s: str, goal: str) -> bool:
    attempt = s
    for _ in range(len(s)):
        attempt = attempt[1:] + attempt[0]
        if attempt == goal:
            return True

    return False


# ChatGPT solution
def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    return goal in (s + s)
