"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99. Find the largest
palindrome made from the product of two 3-digit numbers.

"""


def is_palindromic(n):
    m = n
    reversed = 0
    while n > 0:
        reversed = (reversed * 10) + (n % 10)
        n //= 10
    return m == reversed


def largest_palindrome_from_triple_digit_product():
    largest_palindrome = 0
    i = 999
    while i >= 100:
        if i % 11 == 0:
            j = 999
            k = 1
        else:
            j = 990
            k = 11

        while j >= i:
            if i * j <= largest_palindrome:
                break
            if is_palindromic(i * j):
                largest_palindrome = i * j

            j -= k

        i -= 1

    return largest_palindrome


print(largest_palindrome_from_triple_digit_product())
