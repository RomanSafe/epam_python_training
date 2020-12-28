import pytest

from lecture_11.homework11.tasks.task1 import SimplifiedEnum


def test_simplified_enum_positive():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"


def test_simplified_enum_negative():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("S")

    with pytest.raises(AttributeError) as exc_info:
        SizesEnum.XXL

    assert exc_info.type is AttributeError
    assert exc_info.value.args[0] == "There is not the XXL attribute."
