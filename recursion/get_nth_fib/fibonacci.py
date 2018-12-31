"""
    The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1,
    and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
    Write a function that takes in an integer n and returns the nth Fibonacci number.

   > Sample input: 6
   < Sample output: 5 (0, 1, 1, 2, 3, 5)

"""

# Solution 1: O(2^n) time | O(n) space:


def get_nth_fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return get_nth_fib(n - 1) + get_nth_fib(n - 2)


print(get_nth_fib(6))