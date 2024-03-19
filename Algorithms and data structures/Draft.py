# my solution
def check_record(s: str) -> bool:
    count_a = 0
    count_l = 0
    last = None

    for i in s:
        if count_a > 1 or count_l > 2:
            return False

        if i == "P":
            count_l = 0

        elif i == "A":
            if count_a == 1:
                return False
            count_a += 1
            count_l = 0

        elif i == "L":
            if count_l == 2:
                return False
            elif last == "L":
                count_l += 1
            else:
                count_l = 1

        last = i

    return True


def check_record(s: str) -> bool:
    return False if "LLL" in s or s.count("A") > 1 else True