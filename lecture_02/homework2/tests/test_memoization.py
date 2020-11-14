from collections.abc import Iterable, Mapping
from time import time

import pytest

from lecture_02.homework2.tasks.memoization import cache


@pytest.mark.parametrize("value", [(100, 200)])
def test_cache_1(value: Iterable[int]):
    """With positional arguments."""
    cache_func = cache(lambda a, b: (a ** b) ** 2)

    start_time = time()
    result_1 = cache_func(*value)
    middle_time = time()
    result_2 = cache_func(*value)
    end_time = time()

    assert result_1 == result_2
    assert middle_time - start_time >= end_time - middle_time


@pytest.mark.parametrize("value", [{"a": 50, "b": 70}])
def test_cache_2(value: Mapping[str, int]):
    """With keyword arguments."""
    cache_func = cache(lambda a=0, b=0: (a ** b) ** 2)

    start_time = time()
    result_1 = cache_func(**value)
    middle_time = time()
    result_2 = cache_func(**value)
    end_time = time()

    assert result_1 == result_2
    assert middle_time - start_time >= end_time - middle_time
