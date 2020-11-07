from typing import Sequence

import pytest
from tasks.fibonacci_checker import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((0, 1, 1), True),
        (
            (
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ),
            True,
        ),
        ((2, 2, 4), False),
        ((4182, 4183, 8365), False),
        ((), False),
        ((6765,), True),
        ((-4,), False),
        ((90,), False),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool) -> None:
    actual_result = check_fibonacci(value)
    assert actual_result == expected_result
