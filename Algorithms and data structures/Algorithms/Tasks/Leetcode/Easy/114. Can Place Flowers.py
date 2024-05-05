from typing import List


# my solution
def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    result = 0
    for i in range(len(flowerbed)):
        if n <= result:
            return True

        if i == 0:
            if not any(flowerbed[i:2]):
                flowerbed[i] = 1
                result += 1

        elif not any(flowerbed[i - 1:i + 2]):
            flowerbed[i] = 1
            result += 1

    return n <= result


# ChatGPT solution
def can_place_flowers(flowerbed, n):
    # Copy the flowerbed to avoid modifying the original list
    bed = flowerbed[:]
    # Add 0s to both ends to simplify edge case handling
    bed = [0] + bed + [0]
    # Initialize count of plantable spots
    count = 0

    for i in range(1, len(bed) - 1):
        # Check if the current, previous, and next spots are empty
        if bed[i - 1] == 0 and bed[i] == 0 and bed[i + 1] == 0:
            # Plant a flower
            bed[i] = 1
            # Increment the count
            count += 1
            # If count equals or exceeds n, return True early
            if count >= n:
                return True

    # After checking the entire bed, return whether we could plant at least n flowers
    return count >= n
