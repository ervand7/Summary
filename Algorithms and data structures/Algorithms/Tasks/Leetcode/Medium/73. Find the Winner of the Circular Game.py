def find_the_winner(n: int, k: int) -> int:
    players = list(range(1, n + 1))
    while n > 1:
        for pos in range(1, k + 1):
            idx = (pos - 1) % n
            if pos == k:
                players = players[idx + 1:] + players[:idx]
                n -= 1
                break

    return players[0]


# ChatGPT solution
def find_the_winner(n: int, k: int) -> int:
    winner = 0  # 0-based index

    for i in range(1, n + 1):
        winner = (winner + k) % i

    return winner + 1  # convert to 1-based indexing


print(find_the_winner(n=6, k=5))
