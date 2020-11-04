from typing import List, Tuple

import pytest

from task04.aggregator import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            (
                [-1000000000, 0, 9999999999, 101],
                [0, 0, 0, 0],
                [0, 0, 0, 101],
                [1000000000, 0, -9999999999, 101],
            ),
            3,
        ),
        (
            (
                [-1000000000, 0, 9999999999, 9],
                [-1, 2, 3, 9],
                [2000000000, 0, -9999999999, 9],
                [0, 0, 0, 0],
            ),
            0,
        ),
        (
            (
                [1000000000, 1000000000, 9999999999, 10],
                [1000000000, 1000000000, 9999999999, 10],
                [1000000000, -2000000000, -9999999999, 10],
                [0, 0, 0, 0],
            ),
            1,
        ),
    ],
)
def test_check_sum_of_four(
    value: Tuple[List[int], List[int], List[int], List[int]], expected_result: int
):
    actual_result = check_sum_of_four(*value)

    assert actual_result == expected_result
