from os import getcwd, getenv, remove
from os.path import basename, isfile, join
from typing import Tuple

import pytest

from task03.max_and_min import find_maximum_and_minimum


def create_file(file_name: str, *content) -> str:
    """This function creates text file with given file_name and content.
    Only for current test case!
    """
    file_pathname = join(getcwd(), file_name)
    with open(file_pathname, mode="w+", encoding="utf-8") as file:
        for line in content:
            file.write(line + "\n")
    return file_pathname


def remove_file(file_name: str) -> None:
    """This function removes text file with given file_name.
    I found that removed file appears in project root.
    In this reason I wrote the second part of this function with search and remove.
    Only for current test case!
    """
    if isfile(file_name):
        remove(file_name)

    venv_path = getenv("VIRTUAL_ENV")
    if venv_path:
        project_path = venv_path.rstrip("/env")
    alternative_file_location = join(project_path, basename(file_name))
    if isfile(alternative_file_location):
        remove(alternative_file_location)


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (create_file("test_file1.txt", "1", "2", "3", "4", "5"), (1, 5)),
        (
            create_file(
                "test_file2.txt", "1000000000000", "-2", "0", "4", "-500000000000"
            ),
            (-500000000000, 1000000000000),
        ),
        (create_file("test_file3.txt", "0", "-999999999", "0"), (-999999999, 0)),
        (
            create_file(
                "test_file4.txt",
                "1",
                "4",
                "-5",
                "10",
                "-50",
                "999",
                "92738",
                "8937893739",
            ),
            (-50, 8937893739),
        ),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
    remove_file(value)  # This line only for current test case.
