"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?
"""


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return primes[-1]


print(nth_prime(10001))
