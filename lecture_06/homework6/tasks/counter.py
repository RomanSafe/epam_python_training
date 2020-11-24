"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Class decorator which is applied for any class and attaches to it 2 additional
        methods.

    Returns:
        a new class with additional methods.
    """

    class AddCounter(cls):
        """Attaches to recieved class two additional methods.

        Atribute:
            counter: for storing quantity of class instances.
        """

        counter = 0

        def __init__(self):
            """The constructor of the class. Adds cls.counter increment."""
            super().__init__()
            AddCounter.counter += 1

        def get_created_instances(*args):
            """Returns quantity of created class instances."""
            return AddCounter.counter

        def reset_instances_counter(*args):
            """Reset the cls.counter to zero.

            Returns:
                meaning of cls.counter before reset.
            """

            to_return = AddCounter.counter
            AddCounter.counter = 0
            return to_return

    cls = AddCounter
    return cls


@instances_counter
class User:
    pass
