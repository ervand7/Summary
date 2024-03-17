# my solution
def find_LUS_length(a: str, b: str) -> int:
    return -1 if a == b else max(len(a), len(b))
