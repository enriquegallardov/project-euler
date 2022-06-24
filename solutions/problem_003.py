"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
factor of the number 600851475143 ?

"""


def largest_prime_factor(n):
    if n % 2 == 0:
        last_factor = 2
        n /= 2
        while n % 2 == 0:
            n /= 2
    else:
        last_factor = 1

    factor = 3
    max_factor = n ** 0.5
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n /= factor
            last_factor = factor
            while n % factor == 0:
                n /= factor
            max_factor = n ** 0.5
        factor += 2
    if n == 1:
        return int(last_factor)
    else:
        return int(n)


print(largest_prime_factor(600851475143))
