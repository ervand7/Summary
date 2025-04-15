from typing import List


# my solution
def min_number_of_hours(initial_energy: int, initial_experience: int, energy: List[int], experience: List[int]) -> int:
    time_energy = max(0, sum(energy) + 1 - initial_energy)

    count = 0
    current_experience = initial_experience
    for i in experience:
        if current_experience <= i:
            diff = i + 1 - current_experience
            count += diff
            current_experience += diff
        current_experience += i

    return time_energy + count
