"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
    last_name
    first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import NewType, Union

# for static typing
Timedelta = NewType("Timedelta", datetime.timedelta)


class Homework:
    """An instance contains:

    atributes:
        text, deadline, created (the date and time of creation);

    method:
        is_active.

    """

    def __init__(self, text: str, deadline: int) -> None:
        """Create a class instance.

        Args:
            text: of homework.
            deadline: in days.

        """
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Check is there time till deadline.

        Returns:
            If the deadline has not expired return True, overwise False.

        """
        return datetime.datetime.now() - self.created < self.deadline


class Student:
    """An instance contains:

    atributes:
        first_name, last_name;

    method:
        do_homework.

    """

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create a class instance.

        Args:
            first_name and last_name of a student.

        """
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: Homework) -> Union[Homework, None]:
        """Call the method is_active() of Homework class instance.

        Args:
            homework: Homework class instance.

        Returns:
            True if homework's deadline hasn't expired, overwise False.

        """
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    """An instance contains:

    atributes:
        first_name, last_name;

    staticmethod:
        create_homework.

    """

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create a class instance.

        Args:
            first_name and last_name of a teacher.

        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Create an instance of Homework class.

        Args:
            text: of homework.
            deadline: in days.

        Returns:
            an instance of Homework class.

        """
        return Homework(text, deadline)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
