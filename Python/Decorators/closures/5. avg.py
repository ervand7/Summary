def avg():
    data = []

    def inner(value):
        data.append(value)
        print(sum(data) / len(data))

    return inner


average = avg()
average(10)  # 10
average(11)  # 10.5
average(27)  # 16.0
