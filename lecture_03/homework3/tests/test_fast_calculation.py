from collections.abc import Callable, Iterable
from time import time

import pytest

from lecture_03.homework3.tasks.fast_calculation import fast_sum, slow_calculate


@pytest.mark.parametrize(
    ["function", "iterable", "expected_result", "complete_time"],
    [
        (slow_calculate, (number for number in range(501)), 1025932, 60),
    ],
)
def test_fast_sum(
    function: Callable, iterable: Iterable, expected_result: int, complete_time: int
):
    start_time = time()
    actual_result = fast_sum(function, iterable)
    end_time = time()

    assert actual_result == expected_result
    assert end_time - start_time < complete_time
