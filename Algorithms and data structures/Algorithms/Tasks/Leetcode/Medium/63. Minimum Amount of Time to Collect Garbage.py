from typing import List


def garbage_collection(garbage: List[str], travel: List[int]) -> int:
    houses_count = len(garbage)

    count_m = 0
    count_g = 0
    count_p = 0
    count_distance = 0

    types_houses = {
        "M": 0,
        "G": 0,
        "P": 0,
    }
    for idx, house in enumerate(garbage):
        if "M" in house:
            types_houses["M"] += 1
        if "G" in house:
            types_houses["G"] += 1
        if "P" in house:
            types_houses["P"] += 1

    for idx, house in enumerate(garbage):
        if "M" in house:
            count_m += house.count("M")
            types_houses["M"] -= 1
        if "G" in house:
            count_g += house.count("G")
            types_houses["G"] -= 1
        if "P" in house:
            count_p += house.count("P")
            types_houses["P"] -= 1

        if idx < houses_count - 1:
            if types_houses["M"] > 0:
                count_distance += travel[idx]
            if types_houses["G"] > 0:
                count_distance += travel[idx]
            if types_houses["P"] > 0:
                count_distance += travel[idx]

    return count_m + count_g + count_p + count_distance


#  ChatGPT solution
def garbage_collection(garbage: List[str], travel: List[int]) -> int:
    last = {"M": -1, "G": -1, "P": -1}
    total = 0

    # pickup time + last occurrence
    for i, house in enumerate(garbage):
        total += len(house)
        for c in house:
            last[c] = i

    # prefix travel sum
    prefix = [0] * len(garbage)
    for i in range(1, len(garbage)):
        prefix[i] = prefix[i - 1] + travel[i - 1]

    # add travel time per truck
    for c in ("M", "G", "P"):
        if last[c] > 0:
            total += prefix[last[c]]

    return total


print(garbage_collection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))
