"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.

"""


def sum_of_multiples_below(n, factors):
    return sum(x for x in range(n) if x %
               factors[0] == 0 or x % factors[1] == 0)


print(sum_of_multiples_below(1000, [3, 5]))
