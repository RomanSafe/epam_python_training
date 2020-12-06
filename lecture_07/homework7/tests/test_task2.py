from lecture_07.homework7.tasks.task2 import backspace_compare


def test_backspace_compare_true():
    assert backspace_compare("ab#c", "ad#c") is True
    assert backspace_compare("ab#c", "ad#c") is True
    assert backspace_compare("ab#2$", "ad#2$") is True
    assert backspace_compare("#", "") is True
    assert backspace_compare("", "") is True


def test_backspace_compare_false():
    assert backspace_compare("a#c", "b") is False
    assert backspace_compare("a##**", "*") is False
