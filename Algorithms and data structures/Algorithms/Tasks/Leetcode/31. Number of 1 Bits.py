# ChatGPT solution
def hamming_eight(n: bin) -> int:
    count = 0
    while n:
        count += n & 1  # 1 тут играет роль битовой маски
        n >>= 1  # убираем последнюю цифру (сдвиг вправо)
    return count


print(hamming_eight(0b00000000000000000000000000001011))
