import pytest

from lecture_08.homework8.tasks.task1 import KeyValueStorage


def test_keyvaluestorage_positive():
    storage = KeyValueStorage("lecture_08/homework8/tests/task1.txt")
    storage.new_attribute = "test"

    assert storage.new_attribute == "test"
    assert storage.power == 9001
    assert type(storage.power) is int
    assert storage["name"] == "kek"


def test_keyvaluestorage_builtin_attributes_precedence():
    with open("lecture_08/homework8/tests/task1.txt", "a", encoding="utf-8") as file:
        file.write("__doc__=test\n")
    storage = KeyValueStorage("lecture_08/homework8/tests/task1.txt")

    assert storage.__doc__ != "test"


def test_keyvaluestorage__init__value_error():
    with pytest.raises(ValueError) as exc_info:
        KeyValueStorage("lecture_08/homework8/tests/task1_value_error.txt")

    assert exc_info.type is ValueError
    assert "cannot be assigned to an attribute" in exc_info.value.args[0]


@pytest.fixture
def clean_file_after_test():
    yield 0
    storage = KeyValueStorage("lecture_08/homework8/tests/task1.txt")
    del storage.test_attribute
    storage.rewrite_file()


def test_keyvaluestorage_rewrite_file(clean_file_after_test):
    _ = clean_file_after_test
    storage = KeyValueStorage("lecture_08/homework8/tests/task1.txt")
    storage.test_attribute = "test text"
    storage.rewrite_file()
    storage2 = KeyValueStorage("lecture_08/homework8/tests/task1.txt")

    assert storage2.test_attribute == "test text"
