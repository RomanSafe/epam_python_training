"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """This function returns True if a given sequence is fibonacci sequence, owervise returns False."""
    if not data:
        return False
    for number in data:
        if not is_fibonacci(number):
            return False
    return True


def is_fibonacci(number):
    """This function returns True if a given argument is fibonacci number, owervise returns False."""
    fibonacci_1, fibonacci_2 = 0, 1
    while fibonacci_2 < number:
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
    return fibonacci_2 == number or fibonacci_1 == number
