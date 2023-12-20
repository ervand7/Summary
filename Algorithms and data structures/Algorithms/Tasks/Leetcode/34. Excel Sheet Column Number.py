# my solution
def title_to_number(column_title: str) -> int:
    t = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    result = 0
    counter = 1
    for i in range(len(column_title) - 1, -1, -1):
        if counter == 1:
            result += t[column_title[i]]
        else:
            temp = 1
            for _ in range(1, counter):
                temp *= 26
            result += t[column_title[i]] * temp

        counter += 1

    return result


print(title_to_number("ZY"))