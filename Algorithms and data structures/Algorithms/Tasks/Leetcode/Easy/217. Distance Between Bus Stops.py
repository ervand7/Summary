from typing import List


# my solution
def distance_between_bus_stops(distance: List[int], start: int, destination: int) -> int:
    cw, ccw = 0, 0
    len_distance = len(distance)
    i = start
    while i % len_distance != destination:
        cw += distance[i % len_distance]
        i += 1

    i = start - 1
    while True:
        ccw += distance[i % len_distance]
        if i % len_distance == destination:
            break

        i -= 1

    return min(cw, ccw)


# ChatGPT solution
def distance_between_bus_stops(distance, start, destination):
    if start > destination:
        start, destination = destination, start  # Ensure start < destination for easy slicing

    total_distance = sum(distance)
    clockwise_distance = sum(distance[start:destination])
    counterclockwise_distance = total_distance - clockwise_distance

    return min(clockwise_distance, counterclockwise_distance)
