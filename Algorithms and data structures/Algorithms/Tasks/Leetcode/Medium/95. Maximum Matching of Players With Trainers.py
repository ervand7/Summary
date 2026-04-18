from typing import List


# Time: O(n log n + m log m)
# Space: O(1)
def match_players_and_trainers(players: List[int], trainers: List[int]) -> int:
    players.sort(reverse=True)
    trainers.sort(reverse=True)
    i = 0
    j = 0
    result = 0

    while i < len(players) and j < len(trainers):
        if trainers[j] >= players[i]:
            j += 1
            result += 1

        i += 1

    return result
