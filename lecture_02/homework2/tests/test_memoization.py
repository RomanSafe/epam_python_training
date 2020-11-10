from typing import Literal

import pytest

from lecture_02.homework2.tasks.memoization import cache


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [((100, 200), True), ((50, 70), True)],
)
def test_cache(value: tuple, expected_result: Literal[True]):
    cache_func = cache(lambda a, b: (a ** b) ** 2)
    result_1 = cache_func(*value)
    result_2 = cache_func(*value)

    assert result_1 == result_2
