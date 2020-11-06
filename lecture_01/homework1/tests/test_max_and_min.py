from typing import Tuple

import pytest
from task03.max_and_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("lecture_01/homework1/tests/test_file1.txt", (1, 5)),
        ("lecture_01/homework1/tests/test_file2.txt", (-500000000000, 1000000000000)),
        ("lecture_01/homework1/tests/test_file3.txt", (-999999999, 0)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]) -> None:
    """Test function for the fucnction find_maximum_and_minimum().

    Args:
        value: an argument for the tested function.
        expected_result: for assert statement.
    """
    actual_result = find_maximum_and_minimum(value)
    assert actual_result == expected_result
