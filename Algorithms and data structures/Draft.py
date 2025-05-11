def second_highest(s: str) -> int:
    values = []
    for i in s:
        if i.isnumeric():
            values.append(int(i))

    values = sorted(list(set(values)), reverse=True)
    if values[0] == values[1]:
        return -1

    return values[1]


print(second_highest("unqclirrea85188733589"))
