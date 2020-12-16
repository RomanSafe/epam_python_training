from lecture_09.homework9.tasks.task2 import Suppressor, suppressor


def test_suppressor_class_positive():
    with Suppressor(IndexError):
        print([][2])


def test_suppressor_generator_positive():
    with suppressor(IndexError):
        print([][2])
