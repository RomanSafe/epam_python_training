from typing import List, Tuple

import pytest
from tasks.aggregator import check_sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            (
                [9_999_999_999, -1_000_000_000, 1, 101],
                [0, 0, 0, 0],
                [0, 0, 0, 101],
                [1_000_000_000, -1, -9_999_999_999, 101],
            ),
            36,
        ),
        (
            (
                [-1_000_000_000, 0, 9, 9_999_999_999],
                [-1, 2, 3, 0],
                [2_000_000_000, 0, -9_999_999_999, 9],
                [0, 0, 0, 0],
            ),
            8,
        ),
        (
            (
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ),
            256,
        ),
    ],
)
def test_check_sum_of_four(value: Tuple[List[int], ...], expected_result: int):
    actual_result = check_sum_of_four(*value)

    assert actual_result == expected_result
