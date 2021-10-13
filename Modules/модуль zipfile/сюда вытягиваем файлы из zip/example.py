from tasks import print_hello
from tasks import gen_prime


print_hello()

# primes = gen_prime.delay(10)
primes2 = gen_prime(10)
print(primes2)
# print(primes.get(timeout=2))
# print(primes)
# print(primes.ready())