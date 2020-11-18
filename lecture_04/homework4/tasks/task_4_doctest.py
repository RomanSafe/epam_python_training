"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


>>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"

"""
import math
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Conunts and reterns N FizzBuzz numbers. The first number is "1", and the players
    then count upwards in turn. However, any number divisible by three is replaced by
    the word fizz and any number divisible by five by the word buzz. Numbers divisible
    by 15 become fizz buzz.

    Examples:
        >>> fizzbuzz(5)
        ["1", "2", "fizz", "4", "buzz"]

        >>> fizzbuzz(0)
        Traceback (most recent call last):
        ...
        raise ValueError("n must be >= 1")
        ValueError: n must be >= 1

        >>> fizzbuzz(1.2)
        Traceback (most recent call last):
        raise ValueError("n must be exact integer")
        ValueError: n must be exact integer

    Args:
        n: this number means the last number of Fizzbuzz sequence.

    Returns:
        N FizzBuzz numbers.

    """
    if not n >= 1:
        raise ValueError("n must be >= 1")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    result = []
    for number in range(1, n + 1):
        if number % 3 == 0:
            result.append("fizz")
        elif number % 5 == 0:
            result.append("buzz")
        elif number % 15 == 0:
            result.append("fizz buzz")
        else:
            result.append(str(number))
    return result


""" How to run doctest with the pytest are provided:

- Clone the repository <path your repository>.
- Open terminal and use command <cd path_to_file> to navigate to directory
    where the repository is located.
- Activate virtual environment <source repository_root/env/bin/activate>.
- Install Python >= 3.8 (https://www.python.org/downloads/).
- Install pytest `pip install pytest`.
- Checkout branch <your branch>.
- Invoke pytest directly: <pytest>. By default, pytest will collect test*.txt files
    looking for doctest directives. In addition to text files, you can also execute
    doctests directly from docstrings of your classes and functions, including from
    test modules. For additional information and settings, please, check a link:
    (https://docs.pytest.org/en/stable/doctest.html?highlight=doctest).
 """
