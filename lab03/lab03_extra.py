from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2 or n == 1:
        return n
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        if i == n:
            print(i)
        else:
            print(i)
            return counter(i + 1)
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if a == 0:
        return c
    else:
        return b + ab_plus_c(a-1, b, c)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    # My method

    i = 2
    def divided(i):
        if n % i == 0:
            return i
        else:
            return divided(i + 1)
    flag = divided(i)
    if divided(i) == n:
        print(flag)
        return True
    else:
        print(flag)
        return False

# method in the lab page

#     def helper(i):
#         if i > (n ** 0.5): # Could replace with i == n
#             return True
#         elif n % i == 0:
#             return False
#         return helper(i + 1)
#     return helper(2)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    # Simple recursion

    # if n == 1:
    #     return odd_term(n)
    # else:
    #     if n % 2 == 0:
    #         return even_term(n) + interleaved_sum(n-1, odd_term, even_term)
    #     else:
    #         return odd_term(n) + interleaved_sum(n-1, odd_term, even_term)

    # Use recursion recursion
    def odd_func(n):
        if n == 1:
            return odd_term(n)
        else:
            return odd_term(n) + even_term(n - 1)
    def even_func(n):
        return even_term(n) + odd_term(n - 1)
    if n % 2 == 0:
        return even_func(n)
    else:
        return odd_func(n)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs_helper(10 - n % 10, n // 10) + ten_pairs(n // 10)

def ten_pairs_helper(i, n):
    if n == 0:
        return 0
    else:
        if n % 10 == i:
            return 1 + ten_pairs_helper(i, n // 10)
        else:
            return ten_pairs_helper(i, n // 10)
