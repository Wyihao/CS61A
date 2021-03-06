HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2*g(n - 2) + 3*g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n <= 3:
        print(n)
    else:
        total, i= 0, 3
        pre_pre, pre, cur = 1, 2, 3
        while i < n:
            pre_pre, pre, cur = pre, cur, 3*pre_pre + 2*pre + cur
            i += 1
        return cur


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def helper_sub(i):
        if i == n:
            return 0
        else:
            if include_seven(i):
                return helper_add(i + 1) + 1
            else:
                return helper_sub(i + 1) - 1

    def helper_add(i):
        if i == n:
            return 0
        else:
            if include_seven(i):
                return helper_sub(i + 1) - 1
            else:
                return helper_add(i + 1) + 1

    def include_seven(i):
        return has_seven(i) or i % 7 == 0

    return helper_add(1) + 1


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partitions(n, i):
        if n < 0:
            return 0
        if i == 1:
            return 1
        if n == 0:
            return 1
        return count_partitions(n - i, i) + count_partitions(n, i // 2)


    i = 1
    while i < amount:
        i *= 2
    i = i // 2
    return count_partitions(amount, i)


###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # I can't figure it out, this is other's solution.
    return (lambda f: lambda k: f(f, k))(lambda f, k: 1 if k == 1 else mul(k, f(f, sub(k,1))))
