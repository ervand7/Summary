# my solution
def binary_gap(n: int) -> int:
    def int_to_binary_array(num: int) -> [int]:
        result = []
        while num > 0:
            result.append(num % 2)
            num = num // 2

        return result[::-1]

    binary = int_to_binary_array(n)
    distance = 0
    count_one = 0
    counter = 0
    for i in binary:
        if i == 0:
            if count_one > 0:
                counter += 1

        elif i == 1:
            if count_one > 0:
                counter += 1
                distance = max(distance, counter)
                counter = 0

            else:
                count_one = 1

    return distance


# ChatGPT solution
def binary_gap(n: int) -> int:
    binary_rep = bin(n)[2:]
    max_distance = 0
    prev_index = -1

    for i in range(len(binary_rep)):
        if binary_rep[i] == '1':
            if prev_index != -1:
                distance = i - prev_index
                max_distance = max(max_distance, distance)
            prev_index = i

    return max_distance
