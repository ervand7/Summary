def usual_fact(x):
    counter = 1
    for i in range(1, x + 1):
        counter *= i
        i += 1

    return counter


def rec_fact(x):
    if x == 1:
        return 1
    return rec_fact(x - 1) * x


print(usual_fact(7))  # 5040
print(rec_fact(7))  # 5040
