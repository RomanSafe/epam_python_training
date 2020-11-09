"""
Write down the function, which reads input line-by-line, and find maximum and minimum
values. Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import List, Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Reads given file line-by-line, finds maximum and minimum values in the file.

    Args:
        file_name: path-like file name.

    Returns:
        Tuple with maximum and minimum values.

    """
    with open(file_name) as file:
        line_1 = file.readline()
        minimum_value = min(get_numbers_from_line(line_1))
        maximum_value = max(get_numbers_from_line(line_1))
        for line in file:
            numbers = get_numbers_from_line(line)
            minimum_value = min(minimum_value, *numbers)
            maximum_value = max(maximum_value, *numbers)
    return (minimum_value, maximum_value)


def get_numbers_from_line(string_: str) -> List[int]:
    """Takes given argument, split it, remove delimiter characters and returns.

    Args:
        string: digits separated whitespace
        or whitespace with either comma or semicolon.
        For example "7, 4, 5" or "1 2 3" or "8; 9; 10; 1".

    Returns:
        List of integers.

    """
    return [int(item.strip(",;")) for item in string_.split()]
