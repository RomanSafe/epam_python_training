import datetime

from lecture_05.homework5.tasks.oop_1 import Homework, Student, Teacher


def test_homework():
    fresh_homework = Homework("Make washup", 1)

    assert fresh_homework.text == "Make washup"
    assert fresh_homework.deadline == datetime.timedelta(days=1)
    assert isinstance(fresh_homework, Homework) is True
    assert fresh_homework.is_active() is True


def test_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)

    assert teacher.last_name == "Shadrin"
    assert teacher.first_name == "Daniil"
    assert isinstance(teacher, Teacher) is True
    assert oop_homework.is_active() is True


def test_student(capsys):
    student = Student("Roman", "Petrov")
    fresh_homework = Homework("Learn PEP 8", 2)
    expired_homework = Homework("Install Python", 0)

    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"
    assert isinstance(student, Student) is True
    assert student.do_homework(fresh_homework) is fresh_homework
    assert student.do_homework(expired_homework) is None
    captured = capsys.readouterr()
    assert "You are late" in captured.out
