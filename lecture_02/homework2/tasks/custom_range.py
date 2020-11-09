"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j',
'h']

"""
from typing import Any, List, Sequence


def get_custom_range(entry_iterable: Sequence[Any], *args: Any) -> List[Any]:
    """Accept any iterable of unique values and then it behaves as range function.

    Example:
        assert get_custom_range(
            string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

    Args:
        entry_iterable: any iterable of unique values.
        *args in form:
        get_custom_range(entry_iterable, stop)
        get_custom_range(entry_iterable, start, stop)
        get_custom_range(entry_iterable, start, stop, step)

    Returns:
        List of values depend on recieved arguments.

    """
    result: List[Any] = []  # mypy demanded this annotation.
    if args[0] not in entry_iterable:
        return result

    arguments_amount = len(args)
    if arguments_amount == 1:
        stop = args[0]
        start = entry_iterable[0]
        step = 1
    elif arguments_amount == 2:
        start, stop = args
        step = 1
        if start not in entry_iterable or stop not in entry_iterable:
            return result
    else:
        start, stop, step = args
    start_index = entry_iterable.index(start)
    stop_index = entry_iterable.index(stop)
    for item in entry_iterable[start_index:stop_index:step]:
        result.append(item)
    return result
