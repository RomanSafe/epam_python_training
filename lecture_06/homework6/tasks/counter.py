"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданных экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования

"""
from typing import Any


def instances_counter(cls) -> Any:
    """Decorator which is applied for any class and attaches to it 2 additional
        methods.

    Returns:
        a new class with additional methods.

    """

    def __new__(cls, *args, **kwargs) -> Any:
        """Increments cls._counter by one if a new class instance is created.

        Returns:
            An instance of received class.

        """

        cls._counter += 1
        return super(type(cls), cls).__new__(cls)

    def get_created_instances(cls) -> int:
        """Returns quantity of created class instances."""

        return cls._counter

    def reset_instances_counter(cls) -> int:
        """Reset the cls._counter to zero.

        Returns:
            meaning of the cls._counter before reset.

        """

        to_return = cls._counter
        cls._counter = 0
        return to_return

    setattr(cls, "_counter", 0)
    setattr(cls, "__new__", classmethod(__new__))
    setattr(cls, "get_created_instances", classmethod(get_created_instances))
    setattr(cls, "reset_instances_counter", classmethod(reset_instances_counter))

    return cls


@instances_counter
class User:
    pass
