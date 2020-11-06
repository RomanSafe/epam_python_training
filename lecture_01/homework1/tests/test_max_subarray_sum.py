from typing import List

import pytest
from task05.max_subarray_sum import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([10_000_000, -10, -40, -90, -60, 700_200], 8, 10_700_000),
        ([-1, 3, -1, -3, 5_000_000, -3, -6, 7], 3, 5_000_000),
        ([0, -10, -90, 0, -1, 1, 100, 700_000], 8, 700101),
        ([-1, 3], 3, 3),
    ],
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
    """This function tests a function find_maximal_subarray_sum.

    Args:
        nums: test data located in the first column of decorator arguments.
        k: test data located in the second column of decorator arguments.
        expected_result: in the third column of decorator arguments.
    """
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == expected_result
