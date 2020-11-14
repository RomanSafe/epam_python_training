"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]

"""
from typing import Any, List


def get_combinations(*args: List[Any]) -> List[List]:
    """Takes K lists as arguments and returns Cartesian product of them.

    Cartesian product means all possible lists of K items where the first
    element is from the first list, the second is from the second and so one.

    Returns:
        All possible combinations of items from function's arguments.

    """
    result: List[List] = [[]]
    for list_n in args:
        result = [old_item + [new_item] for old_item in result for new_item in list_n]
    return result
