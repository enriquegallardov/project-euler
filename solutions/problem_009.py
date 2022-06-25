"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find
the product abc.

"""


from math import ceil, gcd


def pythagorean_triplet_with_sum(n):
    s = n // 2
    limit = ceil(s ** 0.5) - 1
    for m in range(2, limit):
        if s % m == 0:
            sm = s // m
            while sm % 2 == 0:
                sm //= 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2 * m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s // (k * m)
                    o = k - m
                    a = d * (m ** 2 - o ** 2)
                    b = 2 * d * m * o
                    c = d * (m ** 2 + o ** 2)
                    return [a, b, c]
                k += 2


result = pythagorean_triplet_with_sum(1000)
print(result[0] * result[1] * result[2])
