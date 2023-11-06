def convertToTitle(num: int) -> str:
    capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    result = []
    while num > 0:
        idx = (num - 1) % 26
        result.append(capitals[idx])
        num = (num - 1) // 26
    result.reverse()
    return ''.join(result)


print(convertToTitle(220))
