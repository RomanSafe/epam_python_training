"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""
from typing import Any, Dict


class SimplifiedEnum(type):
    """Simplified version of Enum class which don't have duplications in variables.

    Makes possible to keep value of attribute equal to its' name.

    """

    def __new__(cls, name: str, bases: tuple, dct: Dict) -> Any:
        """Creates a new class with given name, bases and dct.

        Args:
            name: of new class;
            bases: ancestor class or classes, could be empty;
            dct: name space of new class.

        Returns:
            a new class.

        """

        print(cls, name, bases, dct)
        new_cls = super().__new__(cls, name, bases, dct)
        new_cls.keys = new_cls.__dict__.get(f"_{name}__keys")  # type: ignore
        return new_cls

    def __getattr__(self, name: str) -> str:
        """Implements attribute accesses for instances of the class.

        Args:
            name: of attribute;

        Raises:
            AttributeError: if there is not any attribute with the same name;

        Returns:
            name of attribute, if there is the same key in tuple of keys.

        """

        if name in self.keys:
            return name
        raise AttributeError(f"There is not the {name} attribute.")
