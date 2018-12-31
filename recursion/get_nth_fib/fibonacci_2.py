"""
    The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1,
    and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
    Write a function that takes in an integer n and returns the nth Fibonacci number.

   > Sample input: 6
   < Sample output: 5 (0, 1, 1, 2, 3, 5)

"""
# Solution 2: O(n) time | O(n) space:


def get_nth_fib(n, already_known={1: 0, 2: 1}):
    if n in already_known:
        return already_known[n]
    else:
        already_known[n] = get_nth_fib(n - 1, already_known) + get_nth_fib(n - 2, already_known)
        return already_known[n]


print(get_nth_fib(3))