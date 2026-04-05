from typing import List


# Time: O(n)
# Space: O(1)
def watering_plants(plants: List[int], capacity: int) -> int:
    initial_capacity = capacity
    steps = 0
    for i in range(len(plants)):
        if capacity >= plants[i]:
            steps += 1
        else:
            steps += i
            capacity = initial_capacity
            steps += (i + 1)

        capacity -= plants[i]

    return steps


print(watering_plants(plants=[2, 2, 3, 3], capacity=5))
