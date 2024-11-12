from typing import List


# my solution
def tictactoe(moves: List[List[int]]) -> str:
    vin_positions = (
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},

        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},

        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)},
    )

    player_a = set()
    player_b = set()
    for i, (row, col) in enumerate(moves):
        if i % 2 == 0:
            player_a.add((row, col))
        else:
            player_b.add((row, col))

    for i in vin_positions:
        if len(i & set(player_a)) == 3:
            return "A"
        if len(i & set(player_b)) == 3:
            return "B"

    return "Pending" if len(moves) < 9 else "Draw"
