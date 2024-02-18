def checkPerfectNumber( num: int) -> bool:
    if num <= 1:
        return False

    def findDivisorsOptimal(n):
        divisors = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return list(divisors)


    return sum(findDivisorsOptimal(num)) == num


checkPerfectNumber(28)