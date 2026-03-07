from typing import List
from collections import defaultdict


def finding_users_active_minutes(logs: List[List[int]], k: int) -> List[int]:
    user_minutes = defaultdict(set)

    for user_id, minute in logs:
        user_minutes[user_id].add(minute)

    answer = [0] * k

    for minutes in user_minutes.values():
        uam = len(minutes)
        answer[uam - 1] += 1

    return answer
