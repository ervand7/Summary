from typing import List


# my solution
def lemonade_change(bills: List[int]) -> bool:
    h = {5: 0, 10: 0, 20: 0}
    for i in bills:
        if i == 5:
            h[5] += 1

        if h[5] == 0:
            return False

        elif i == 10:
            h[5] -= 1
            h[10] += 1

        elif i == 20:
            if h[10] == 0:
                if h[5] < 3:
                    return False
                h[5] -= 3
                h[20] += 1

            elif h[10] >= 1:
                h[10] -= 1
                h[5] -= 1
                h[20] += 1

    return True


# ChatGPT solution
def lemonade_change(bills):
    five_count = 0
    ten_count = 0

    for bill in bills:
        if bill == 5:
            five_count += 1
        elif bill == 10:
            if five_count > 0:
                five_count -= 1
                ten_count += 1
            else:
                return False
        elif bill == 20:
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False

    return True
