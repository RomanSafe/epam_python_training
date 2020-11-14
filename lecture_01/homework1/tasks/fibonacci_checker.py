"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Checks given sequence is fibonacci or not.

    Args:
        data: sequence contains >= 0 integers inside.

    Returns:
        True if a given sequence is fibonacci sequence, owervise False.

    """
    if not data:
        return False
    fibonacci_1, fibonacci_2 = 0, 1
    for number in data:
        while True:
            if number < fibonacci_1:
                return False
            elif number == fibonacci_1:
                fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
                break
            else:
                fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
    return True
