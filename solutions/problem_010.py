"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_below(n):
    sum = 0
    for i in range(0, n):
        sum += i if is_prime(i) else 0
        
    return sum

print(sum_of_primes_below(2000000))