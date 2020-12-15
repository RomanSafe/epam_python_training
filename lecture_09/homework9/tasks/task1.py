"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from itertools import chain
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merges integers from sorted files and yields a generator iterator with sorted
        integers.

    Using:
        >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
        [1, 2, 3, 4, 5, 6]

    Args:
        file_list: list with paths to files for merge.

    Yields:
        generator iterator with sorted integers.

    """

    def _get_iterator_from_file(file_name: Union[Path, str]) -> Iterator:
        """Reads file line by line and yields a generator iterator with integers.

        Args:
            file_name: path to a file.

        Yields:
            generator iterator with sorted integers.

        """

        if isinstance(file_name, str):
            file_name = Path(file_name)
        with file_name.open() as file:
            for line in file:
                yield int(line.rstrip())

    def _merge_two_iterators(iterator_1: Iterator, iterator_2: Iterator) -> Iterator:
        """Merges two iterators and yields generator iterator with sorted integers.

        Args:
            iterator_1: with integers to merge;
            iterator_2: with integers to merge.

        Yields:
            generator iterator with sorted integers.

        """

        number_1 = next(iterator_1)
        number_2 = next(iterator_2)
        while True:
            try:
                if number_1 < number_2:
                    yield number_1
                    number_1 = next(iterator_1)
                elif number_1 == number_2:
                    yield from (number_1, number_2)
                    number_1 = next(iterator_1)
                    number_2 = next(iterator_2)
                else:
                    yield number_2
                    number_2 = next(iterator_2)
            except StopIteration:
                yield max(number_1, number_2)
                yield from chain(iterator_1, iterator_2)
                break

    iterator_1 = _get_iterator_from_file(file_list.pop())
    print(type(iterator_1))
    iterator_2 = _get_iterator_from_file(file_list.pop())
    while file_list:
        iterator_1 = _merge_two_iterators(iterator_1, iterator_2)
        iterator_2 = _get_iterator_from_file(file_list.pop())
    yield from _merge_two_iterators(iterator_1, iterator_2)
