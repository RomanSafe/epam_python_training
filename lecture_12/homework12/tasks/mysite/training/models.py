from django.db import models
from django.utils import timezone


class Person(models.Model):
    """Abstract base class. Keeps common information for a number of other models.

    Describes an instance of a person. Base class for Student and Teacher classes.

    Attributes:
        first_name: the name of a person;
        last_name: the surname of a person.

    """

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Student(Person):
    """Describes an instance of a student.

    Attributes:
        first_name: the name of a student;
        last_name: the surname of a student.

    """


class Teacher(Person):
    """Describes an instance of a teacher.

    Attributes:
        first_name: the name of a teacher;
        last_name: the surname of a teacher.

    """


class Homework(models.Model):
    """Describes an instance of homework.

    Attributes:
        text: text of the current homework;

        deadline: a datetime.datetime object pointed to deadline for the
        current homework;

        created: the date and time of the instance's creation.

    """

    text = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now)


class HomeworkResult(models.Model):
    """Describes result of a homework.

    Attributes:
        homework: an instance of the Homework class;

        solution: a string representing a solution of the given homework. A good
        solution should consist of 6 symbols at least;

        author: an instance of the Student class;

        created: the date and time of the instance's creation.

    """

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=100)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
