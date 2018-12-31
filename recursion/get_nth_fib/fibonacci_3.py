"""
    The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1,
    and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
    Write a function that takes in an integer n and returns the nth Fibonacci number.

   > Sample input: 6
   < Sample output: 5 (0, 1, 1, 2, 3, 5)

"""
# Solution 3: O(n) time | O(1) space:


def get_nth_fib(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[0] if n < 2 else last_two[1]


print(get_nth_fib(6))