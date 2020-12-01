"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда попадают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гарантировать отсутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант использования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпляр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.

"""
from __future__ import annotations

import datetime
from collections import defaultdict
from typing import NewType

# for static typing
Timedelta = NewType("Timedelta", datetime.timedelta)


class Error(Exception):
    """Base class for exceptions in this module."""


class HomeworkError(Error):
    """Raised when the class HomeworkResult hadn't received the Homework class as the
    homework argument.

    Attribute:
        message: explanation of the exception. Defaults to None.

    """

    def __init__(self, message=None) -> None:
        """Initialises a class instance."""

        self.message = message


class DeadlineError(Error):
    """Raised when homework.is_active() returns False.

    Attribute:
        message: explanation of the exception. Defaults to None.

    """

    def __init__(self, message=None) -> None:
        """Initialises a class instance."""

        self.message = message


class Homework:
    """Describes an instance of homework.

    Attributes:
        text: text of the current homework;

        deadline: a datetime.timedelta object with quantity days till deadline for the
        current homework;

        created: the date and time of the instance's creation.

    """

    def __init__(self, text: str, deadline: int) -> None:
        """Initialise a class instance."""
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Checks is there time till deadline of the current homework.

        Returns:
            If the deadline has not expired return True, otherwise False.

        """

        return datetime.datetime.now() - self.created < self.deadline

    def __hash__(self) -> int:
        """Called by built-in function hash() and is used for operations on members of
        hashed collections including set, frozenset, and dict.

        Returns:
            the hash value of the text and deadline attributes'.

        """

        return hash((self.text, self.deadline))

    def _is_valid_operand(self, other: Homework) -> bool:
        """Validates the operand for equally check."""
        return hasattr(other, "text") and hasattr(other, "deadline")

    def __eq__(self, other: Homework) -> bool:  # type: ignore[override]
        """Defines the behaviour when equal comparison operator is called.

        Args:
            other: the second operand for comparison.

        Returns:
            True is compared attributes are equal, otherwise False.

        """

        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.text.lower(), self.deadline) == (
            other.text.lower(),
            other.deadline,
        )


class Person:
    """Describes an instance of a person. Base class for Student and Teacher classes.

    Attributes:
        first_name: the name of a person;
        last_name: the surname of a person.

    """

    def __init__(self, first_name: str, last_name: str) -> None:
        """Initialises a class instance."""
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """Describes an instance of a student.

    Attributes:
        first_name: the name of a student;
        last_name: the surname of a student.

    Raises:
        DeadlineError: if deadline of the homework has expired.

    """

    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        """Checks is the deadline of the given homework expired or not.

        Args:
            homework: an instance of the Homework class that a student is going to do;

            solution: a string representing a solution of the given homework.

        Returns:
            an instance of the HomeworkResult class if it's deadline hasn't
            expired.

        Raises:
            DeadlineError if deadline of the homework has expired.

        """

        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late")


class HomeworkResult:
    """Describes result of a homework.

    Attributes:
        author: an instance of the Student class;

        homework: an instance of the Homework class;

        solution: a string representing a solution of the given homework. A good
        solution should consist of 6 symbols at least;

        created: the date and time of the instance's creation.

    """

    def __init__(self, author: Student, homework: Homework, solution: str) -> None:
        """Initialises a class instance.

        Raises:
            HomeworkError: if given homework argument not a Homework object.

        """

        if not isinstance(homework, Homework):
            raise HomeworkError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()

    def __hash__(self) -> int:
        """Called by built-in function hash() and is used for operations on members of
        hashed collections including set, frozenset, and dict.

        Returns:
            the hash value of the solution attribute's.

        """

        return hash(self.solution)

    def _is_valid_operand(self, other: HomeworkResult) -> bool:
        """Validates the operand for equally check."""
        return hasattr(other, "solution") and hasattr(other, "homework")

    def __eq__(self, other: HomeworkResult) -> bool:  # type: ignore[override]
        """Defines the behaviour when equal comparison operator is called.

        Args:
            other: the second operand for comparison.

        Returns:
            True is compared attributes are equal, otherwise False.

        """

        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.solution.lower(), self.homework) == (
            other.solution.lower(),
            other.homework,
        )


class Teacher(Person):
    """Describes an instance of a teacher.

    Class attribute:
        homework_done: a data structure with dictionary interface. All HomeworkResult
        objects are saved here after successful applying of check_homework method's.
        Homework objects are keys and HomeworkResult objects are values. It's
        guaranteed that for every homework there are only unique results.

    Attributes:
        first_name: the name of a teacher;
        last_name: the surname of a teacher.

    """

    homework_done = defaultdict(set)  # type: ignore

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Creates an instance of the Homework class.

        Args:
            text: a text of the created homework.
            deadline: a term to complete the homework in days.

        Returns:
            an instance of Homework class.

        """

        return Homework(text, deadline)

    @staticmethod
    def check_homework(homework_result: HomeworkResult) -> bool:
        """Checks the given homework result.

        Args:
            homework_result: an instance of the HomeworkResult class.

        Returns:
            True if the solution of the given homework result more then 5 symbols.
            Otherwise, False.

        """

        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @staticmethod
    def reset_results(homework: Homework = None) -> None:
        """Resets results of homework. If an argument is given, this method removes
        results for this homework. If the method is called without an argument, it
        cleans whole homework_done dictionary.

        Args:
            homework: an instance of the Homework class. Defaults to None.

        """

        if homework:
            Teacher.homework_done.pop(homework, None)
        else:
            Teacher.homework_done.clear()
