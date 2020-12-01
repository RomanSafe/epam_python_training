import datetime

from pytest import raises

from lecture_06.homework6.tasks.oop_2 import (
    DeadlineError,
    Homework,
    HomeworkError,
    HomeworkResult,
    Student,
    Teacher,
)


def test_teacher_instance_attributes():
    oop_teacher = Teacher("Daniil", "Shadrin")
    assert oop_teacher.first_name == "Daniil"
    assert oop_teacher.last_name == "Shadrin"


def test_student_instance_attributes():
    good_student = Student("Lev", "Sokolov")
    assert good_student.first_name == "Lev"
    assert good_student.last_name == "Sokolov"


def test_teacher_create_homework():
    oop_teacher = Teacher("Daniil", "Shadrin")
    oop_hw = oop_teacher.create_homework("Learn OOP", 1)
    assert isinstance(oop_hw, Homework)
    assert oop_hw.text == "Learn OOP"
    assert oop_hw.deadline == datetime.timedelta(days=1)


def test_homework_result_negative():
    good_student = Student("Lev", "Sokolov")
    with raises(HomeworkError) as exc_info:
        HomeworkResult(good_student, "not_a_homework_obj", "hmmm...")

    assert exc_info.type is HomeworkError
    assert exc_info.value.args[0] == "You gave a not Homework object"


def test_homework_result_positive():
    student = Student("Lev", "Sokolov")
    homework = Homework("Read OOP.", 2)
    done_homework = HomeworkResult(student, homework, "I've read it twice.")

    assert done_homework.homework is homework
    assert done_homework.solution == "I've read it twice."
    assert done_homework.author is student


def test_student_do_homework_negative():
    student = Student("Lev", "Sokolov")
    homework = Homework("Old task.", 0)
    with raises(DeadlineError) as exc_info:
        student.do_homework(homework, "some solution")

    print(exc_info.value)
    assert exc_info.type is DeadlineError
    assert exc_info.value.args[0] == "You are late"


def test_student_do_homework_positive():
    student = Student("Lev", "Sokolov")
    homework = Homework("New task.", 7)

    assert isinstance(student.do_homework(homework, "some solution"), HomeworkResult)


def test_teacher_check_homework_return_true():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Lev", "Sokolov")
    homework = Homework("Read OOP principles.", 2)
    done_homework = HomeworkResult(student, homework, "Pretty long solution.")

    assert teacher.check_homework(done_homework) is True


def test_teacher_check_homework_return_false():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Lev", "Sokolov")
    homework = Homework("Read OOP.", 2)
    bad_solution = HomeworkResult(student, homework, "done")

    assert teacher.check_homework(bad_solution) is False


def test_teacher_homework_done():
    teacher_1 = Teacher("Daniil", "Shadrin")
    teacher_2 = Teacher("Aleksandr", "Smetanin")
    student_1 = Student("Lev", "Sokolov")
    student_2 = Student("Ivan", "Petrov")
    homework = Homework("Read OOP.", 2)
    done_homework = HomeworkResult(student_1, homework, "I've read it twice.")
    copied_homework = HomeworkResult(student_2, homework, "I've read it twice.")
    teacher_1.check_homework(done_homework)
    teacher_2.check_homework(copied_homework)

    assert teacher_1.homework_done == teacher_2.homework_done
    assert done_homework in teacher_1.homework_done[homework]
    teacher_1.homework_done[homework].discard(done_homework)
    assert len(teacher_1.homework_done[homework]) == 0


def test_teacher_reset_results():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Lev", "Sokolov")
    homework_1 = Homework("Read OOP.", 2)
    done_homework_1 = HomeworkResult(student, homework_1, "I've read it twice.")
    teacher.check_homework(done_homework_1)
    homework_2 = Homework("Read smth.", 3)
    done_homework_2 = HomeworkResult(student, homework_2, "I've learned it.")
    teacher.check_homework(done_homework_2)

    assert done_homework_1 in teacher.homework_done[homework_1]
    teacher.reset_results(homework_1)
    assert done_homework_1 not in teacher.homework_done[homework_1]

    assert done_homework_2 in teacher.homework_done[homework_2]
    teacher.reset_results()
    assert len(teacher.homework_done) == 0
