"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Generator, Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """This function checks given sequence is fibonacci or not.

    Args:
        data: sequence contains >= 0 integers inside.

    Returns:
        True if a given sequence is fibonacci sequence, owervise False.
    """
    if not data:
        return False
    fibonacci_generator = generate_closest_fibonacci(data[0])
    for number in data:
        if number != next(fibonacci_generator):
            return False
    return True


def generate_closest_fibonacci(begining: int) -> Generator:
    """This function generates fibonacci sequence, which begins from
        fibonacci number closest to the given argument.

    Args:
        begining: closest number for begining of the sequence.

    Yields:
        the fibonacci sequence number by number.
    """
    fibonacci_1, fibonacci_2 = 0, 1
    while True:
        if fibonacci_1 >= begining:
            yield fibonacci_1
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
