from os.path import exists

import pytest

from lecture_04.homework4.tasks.task_1_read_file import read_magic_number

temp_paths = []


@pytest.fixture(params=["2", "1"])
def create_test_file_true(tmp_path, request):
    global temp_paths
    dir = tmp_path / "for_tests"
    dir.mkdir()
    file = dir / "for_tests.txt"
    content = request.param
    file.write_text(content)
    path = file.resolve()
    temp_paths.append(path)
    yield path, file, content
    file.unlink()
    dir.rmdir()


def test_read_magic_number_true(create_test_file_true):
    path, test_file, content = create_test_file_true

    assert test_file.exists() is True
    assert test_file.read_text() == content
    assert read_magic_number(path) is True


@pytest.fixture(params=["0", "3", "a"])
def create_test_file_false(tmp_path, request):
    global temp_paths
    dir = tmp_path / "for_tests"
    dir.mkdir()
    file = dir / "for_tests.txt"
    content = request.param
    file.write_text(content)
    path = file.resolve()
    temp_paths.append(path)
    yield path, file, content
    file.unlink()
    dir.rmdir()


def test_read_magic_number_false(create_test_file_false):
    path, test_file, content = create_test_file_false

    assert test_file.exists() is True
    assert test_file.read_text() == content
    assert read_magic_number(path) is False


def test_read_magic_number_exception():
    with pytest.raises(ValueError) as excinfo:
        read_magic_number("not_such_path")

    assert "ValueError" in str(excinfo.type)
    assert "Some error has happened." in str(excinfo.value)


def test_are_temporaty_files_exist():
    for path in temp_paths:
        assert exists(path) is False
