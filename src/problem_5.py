"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?

"""


def smallest_number_evenly_divisible_by_range(n):
    m = n
    while True:
        if all(n % i == 0 for i in range(1, m + 1)):
            return n
        else:
            n += m


print(smallest_number_evenly_divisible_by_range(20))
