from pathlib import Path

from lecture_09.homework9.tasks.task3 import universal_file_counter


def test_universal_file_counter_positive():
    assert universal_file_counter(Path("lecture_09/homework9/tests"), "txt") == 10
    assert (
        universal_file_counter(Path("lecture_09/homework9/tests"), "txt", str.split)
        == 14
    )
