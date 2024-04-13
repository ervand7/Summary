# my solution
def count_prime_set_bits(left: int, right: int) -> int:
    def int_to_bin_array(num) -> list:
        binary = []
        while num > 0:
            binary.append(num % 2)
            num = num // 2
        return reversed(binary)

    result = 0
    for i in range(left, right + 1):
        value = sum(int_to_bin_array(i))
        if value == 1:
            continue

        flag = True
        for j in range(2, value + 1):
            if 1 < j < value:
                if value % j == 0:
                    flag = False
                    break

        if flag == True:
            result += 1

    return result


# my solution using built-in bin func (fast)
def count_prime_set_bits(left: int, right: int) -> int:
    result = 0
    for i in range(left, right + 1):
        value = bin(i).count('1')
        if value == 1:
            continue

        flag = True
        for j in range(2, value + 1):
            if 1 < j < value:
                if value % j == 0:
                    flag = False
                    break

        if flag == True:
            result += 1

    return result


# ChatGPT very fast but hard to read solution
def count_prime_set_bits(left, right):
    # Sieve of Eratosthenes to determine prime numbers up to 20
    max_bits = 20
    sieve = [True] * (max_bits + 1)
    sieve[0], sieve[1] = False, False
    for start in range(2, int(max_bits ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_bits + 1, start):
                sieve[multiple] = False
    primes = {i for i in range(max_bits + 1) if sieve[i]}

    # Count numbers with a prime number of set bits
    count = 0
    for num in range(left, right + 1):
        # Calculate number of set bits using bit manipulation
        set_bits = bin(num).count('1')
        if set_bits in primes:
            count += 1

    return count
