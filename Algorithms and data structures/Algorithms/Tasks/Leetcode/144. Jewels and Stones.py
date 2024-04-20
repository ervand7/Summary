# my solution
def num_jewels_in_stones(jewels: str, stones: str) -> int:
    jewels = set(jewels)
    result = 0
    for i in stones:
        if i in jewels:
            result += 1

    return result
