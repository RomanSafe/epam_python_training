import pytest

from lecture_11.homework11.tasks.task1 import SimplifiedEnum


def test_simplified_enum_positive():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"


def test_simplified_enum_negative():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("S", "M")

    with pytest.raises(AttributeError) as exc_info:
        SizesEnum.XXL

    assert exc_info.type is AttributeError
    assert exc_info.value.args[0] == "type object 'SizesEnum' has no attribute 'XXL'"


def test_simplified_enum_attribute_assignment():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("S",)

    SizesEnum.M = "M"

    assert SizesEnum.M == "M"


def test_simplified_enum_len():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED",)

    ColorsEnum.BLACK = "BLACK"

    assert len(ColorsEnum) == 2


def test_simplified_enum_iterable():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert [item for item in ColorsEnum] == ["RED", "BLUE", "ORANGE", "BLACK"]
