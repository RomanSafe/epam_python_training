# I decided to write a code that generates data filtering object from a list of keyword
# parameters:
from collections.abc import Callable, Hashable
from typing import Any, List


class Filter:
    """Helper filter class. Accepts a list of single-argument functions that return
    True if object in list of data conforms to some criteria, otherwise False.

    """

    def __init__(self, functions: List[Callable]):
        self.functions = functions

    def apply(self, data: list) -> List[Any]:
        """Takes list of items to filter and apply the list of functions to them as
        filter criteria.

        Args:
            data: list of items to filter.

        Returns:
            list of filtered items.

        """
        return [
            item
            for item in data
            if all([function(item) for function in self.functions])
        ]


# example of usage:
# positive_even = Filter([lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a,
# int)])
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords: Hashable) -> Filter:
    """Makes a filter from gived keyword arguments.

    Returns:
        Filter object.

    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(dictionary):
            return dictionary[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

# make_filter(name='polly', type='bird').apply(sample_data) should return only second
# entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
