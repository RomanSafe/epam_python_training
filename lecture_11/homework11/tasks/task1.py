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
from collections.abc import Generator
from typing import Any, Dict, Optional


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

        members = dct.get(f"_{name}__keys")
        if members:
            dct["members"] = {key: key for key in members}
        else:
            dct["members"] = {}
        new_cls = type.__new__(cls, name, bases, dct)
        return new_cls

    def __getattribute__(self, name: str) -> Optional[Any]:
        """Implements attribute accesses for instances of the class.

        Args:
            name: of attribute;

        Raises:
            AttributeError: if object has no attribute name;

        Returns:
            attribute, if is.

        """

        try:
            return type.__getattribute__(self, name)
        except AttributeError as error:
            try:
                return self.__dict__["members"][name]
            except KeyError:
                raise error

    def __setattr__(self, name: str, value: str) -> None:
        """Setts an attribute.

        Args:
            name: of the attribute;
            value: of the attribute.

        """

        self.__dict__["members"][name] = value

    def __len__(self) -> int:
        """[summary]

        [extended_summary]

        Returns:
            length of "members" dictionary.

        """

        return len(self.__dict__["members"])

    def __iter__(self) -> Generator[str, None, None]:
        """Called when an iterator is required for the "members" dictionary.

        Yields:
            iterator object which iterates over the keys of the "members" dictionary.

        """

        yield from self.__dict__["members"]
