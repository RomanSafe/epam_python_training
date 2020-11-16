import pytest

from lecture_03.homework3.tasks.armstrong import is_armstrong


@pytest.mark.parametrize("value", [153])
def test_is_armstrong_true(value: int):
    assert is_armstrong(value) is True, "Is Armstrong number"


@pytest.mark.parametrize("value", [10])
def test_is_armstrong_false(value: int):
    assert is_armstrong(value) is False, "Is not Armstrong number"
