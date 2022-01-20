"""
// ========== пример вызова функции внутри другой функции ==========
function showPrimes(n) {
    for (let i = 2; i < n; i++) {
        if (!isPrime(i)) continue;
        console.log(i);
    }
}


function isPrime(n) {
    for (let i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
"""


def is_prime(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return True
        return False


def show_primes(n):
    for i in range(2, n):
        if i == 2:
            print(i)
        if is_prime(i):
            continue
        print(i)


show_primes(200)
