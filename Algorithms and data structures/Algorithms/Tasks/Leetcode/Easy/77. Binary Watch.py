from typing import List


def read_binary_watch(turned_on: int) -> List[str]:
    def count_set_bits(num):
        # Count the number of set bits (1s) in the binary representation of num
        count = 0
        while num:
            count += num % 2
            num //= 2
        return count

    result = []
    for h in range(12):
        for m in range(60):
            if count_set_bits(h) + count_set_bits(m) == turned_on:
                # Format the time correctly, ensuring minutes have two digits
                time = f"{h}:{m:02d}"
                result.append(time)

    return result


print(read_binary_watch(1))