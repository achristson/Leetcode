"""
Fibonacci numbers

1 1 2 3 5 8 13 ...
Each number is the sum of the previous two
And you start with 1 and 1

Write a program that given n gives you the n'th fib number.
"""


def fibonacci(n):
    """basic Solution"""
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


"""
Time: O(2^n)
Space: O(n)
"""


cache = {}
cache[1] = 1
cache[2] = 1


def fibonacci_memo(n):
    """Memoization Solution"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return cache[n]


"""
Time: O(n)
Space: O(n)
"""


def fibonacci_dp(n):
    """Dynamic Programming Solution"""
    if n == 1 or n == 2:
        return 1

    table = [0 for _ in range(n + 1)]
    table[1] = 1
    table[2] = 1

    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


"""
Time: O(n)
Space: O(n)
"""


def fibonacci_dp_constant_space(n):
    """Dynamic Programming Solution with constant space"""
    if n == 1 or n == 2:
        return 1

    table = [0] * 3
    table[1] = 1
    table[2] = 1

    for i in range(3, n+1):
        table[i % 3] = table[(i - 1) % 3] + table[(i - 2) % 3]
    return table[n % 3]


"""
Time: O(n)
Space: O(1)
"""
