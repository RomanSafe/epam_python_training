from typing import List, Tuple

import pytest

from lecture_02.homework2.tasks.cartesian_product import get_combinations


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
        (
            (["a", "b"], ["c", "d"], ["e", "f"]),
            [
                ["a", "c", "e"],
                ["a", "c", "f"],
                ["a", "d", "e"],
                ["a", "d", "f"],
                ["b", "c", "e"],
                ["b", "c", "f"],
                ["b", "d", "e"],
                ["b", "d", "f"],
            ],
        ),
    ],
)
def test_get_combinations(value: Tuple[List], expected_result: bool):
    actual_result = get_combinations(*value)

    assert actual_result == expected_result
