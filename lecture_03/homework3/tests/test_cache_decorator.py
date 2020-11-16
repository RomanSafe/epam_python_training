from random import randint
from time import time

from lecture_03.homework3.tasks.cache_decorator import cache


def test_cache_void_args():
    @cache(times=2)
    def f():
        return randint(2, 500) ** randint(300, 400)

    start_time = time()
    result_1 = f()
    res_1_time = time()

    result_2 = f()
    res_2_time = time()

    result_3 = f()
    res_3_time = time()

    result_4 = f()

    assert result_1 == result_2 == result_3
    assert result_4 != result_3
    assert res_1_time - start_time > res_2_time - res_1_time
    assert res_1_time - start_time > res_3_time - res_2_time


def test_cache_with_args():
    @cache(times=2)
    def f(number1, number2=2):
        return randint(2, 100) ** number1 ** number2

    start_time = time()
    result_1 = f(50)
    res_1_time = time()

    result_2 = f(50)
    res_2_time = time()

    result_3 = f(50)
    res_3_time = time()

    result_4 = f(80)

    assert result_1 == result_2 == result_3
    assert result_4 != result_3
    assert res_1_time - start_time > res_2_time - res_1_time
    assert res_1_time - start_time > res_3_time - res_2_time
