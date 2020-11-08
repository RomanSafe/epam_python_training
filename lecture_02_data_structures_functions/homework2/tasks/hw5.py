"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, Iterable, List


def get_custom_range(entry_iterable: Iterable[Any], stop=None, start=None, step=1) -> List[Any]:
    """get_custom_range.

    Args:
        entry_iterable: [description]
        stop: [description]. Defaults to entry_iterable[-1].
        start: [description]. Defaults to entry_iterable[0].
        step: [description]. Defaults to 1.

    """
    result = []
    if stop is None:
        stop = 
    if start is None:
        start = 
    for item in entry_iterable:
        if item == stop:
            return result
        result.append(item)