"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
factor of the number 600851475143 ?

"""


def largest_prime_factor(n):
    factors = []
    factor = 2
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n /= factor
        else:
            factor += 1
    print(factors)
    return factors[-1]


print(largest_prime_factor(600851475143))
