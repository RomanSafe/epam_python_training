"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """This function returns True if a given sequence is fibonacci sequence, owervise returns False."""
    if not data:
        return False
    fibonacci_generator = generate_closest_fibonacci(data[0])
    for number in data:
        if number != next(fibonacci_generator):
            return False
    return True


def generate_closest_fibonacci(begining: int):
    """This function takes an intiger number and yields the fibonacci sequence, which begins from
    fibonacci number closest to the given number.
    """
    fibonacci_1, fibonacci_2 = 0, 1
    while True:
        if fibonacci_1 >= begining:
            yield fibonacci_1
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
