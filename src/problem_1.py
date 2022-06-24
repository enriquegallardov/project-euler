"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.

"""


def sum_of_multiples_below(n, factor):
    p = (n - 1) // factor
    return factor * (p * (p + 1)) // 2


print(sum_of_multiples_below(1000, 3) +
      sum_of_multiples_below(1000, 5) - sum_of_multiples_below(1000, 15))
