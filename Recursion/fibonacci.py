"""
Fibonacci numbers

1 1 2 3 5 8 13 ...
Each number is the sum of the previous two
And you start with 1 and 1

Write a program that given n gives you the n'th fib number.
"""
# Memoization solution:
cache = {}
cache[1] = 1
cache[2] = 1


def fibonacci(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

# Dynamic Programming Solution:


def fibonacci_dp(n):
    if n == 1 or n == 2:
        return 1

    table = [0 for _ in range(n+1)]
    table[1] = 1
    table[2] = 1

    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]
