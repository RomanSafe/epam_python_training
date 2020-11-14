"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def get_major_and_minor_elem(array_: List) -> Tuple[int, int]:
    """Returns the most common and the least common elements from a given list.

    Args:
        array_: should be non-empty and the most common element always exist in the
        array. The most common element appears more than n // 2 times. The least
        common element appears fewer than other.

    Returns:
        Tuple with the most common and the least common elements.

    """
    counter: dict = {}
    for item in array_:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    items_list = sorted(counter, key=lambda key_: counter[key_])
    return items_list[-1], items_list[0]
