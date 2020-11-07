"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Any, List, Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """This function reads given file line-by-line, finds maximum and minimum values in the file.

    Args:
        file_name: path-like file name.

    Returns:
        Tuple with maximum and minimum values.
    """
    with open(file_name) as file:
        line_1: str = file.readline()
        minimum_value: Any = min(convert_str_to_int(line_1))
        maximum_value: Any = max(convert_str_to_int(line_1))
        for line in file:
            numbers: Tuple[int, ...] = convert_str_to_int(line)
            minimum_value = min(minimum_value, *numbers)
            maximum_value = max(maximum_value, *numbers)
    return (minimum_value, maximum_value)


def convert_str_to_int(string_: str) -> Tuple[int, ...]:
    """This function cleans given argument, converts it and returns.

    Args:
        string: digits separated whitespace and or comma, semicolon, colon.

    Returns:
        Tuple of integers.
    """
    return tuple((int(item.strip(",;:")) for item in string_.split()))
