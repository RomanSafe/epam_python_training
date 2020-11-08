from typing import List, Tuple

import pytest
from tasks.cartesian_product import get_combinations


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            ([1, 2], [3, 4]),
            [
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
            ],
        ),
    ],
)
def test_get_combinations(value: Tuple[List], expected_result: bool):
    actual_result = get_combinations(*value)

    assert actual_result == expected_result
