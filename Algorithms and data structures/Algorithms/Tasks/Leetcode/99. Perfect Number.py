def check_perfect_number(num: int) -> bool:
    def find_divisors(n):
        divisors = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return divisors

    return sum(find_divisors(num)) - num == num


print(check_perfect_number(28))
