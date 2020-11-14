from typing import List

import pytest

from lecture_02.homework2.tasks.text_processing import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            "lecture_02/homework2/tests/data.txt",
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "politisch-strategischen",
                "Selbstverständlich",
                "résistance-Bewegungen",
                "Fingerabdrucks",
                "Friedensabstimmung",
            ],
        ),
        (
            "lecture_02/homework2/tests/little_data.txt",
            [
                "vorgebahnte",
                "Betrachtung",
                "ausführen",
                "verbirgt",
                "vielmehr",
                "bedenkli",
                "Waldgang",
                "hinter",
                "Ausflug",
                "gefaßt",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(value: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("lecture_02/homework2/tests/data.txt", "›"),
        ("lecture_02/homework2/tests/little_data.txt", "W"),
    ],
)
def test_get_rarest_char(value: str, expected_result: str):
    actual_result = get_rarest_char(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("lecture_02/homework2/tests/data.txt", 5305),
        ("lecture_02/homework2/tests/little_data.txt", 7),
    ],
)
def test_count_punctuation_chars(value: str, expected_result: int):
    actual_result = count_punctuation_chars(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("lecture_02/homework2/tests/data.txt", 2972),
        ("lecture_02/homework2/tests/little_data.txt", 6),
    ],
)
def test_count_non_ascii_chars(value: str, expected_result: int):
    actual_result = count_non_ascii_chars(value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("lecture_02/homework2/tests/data.txt", "ä"),
        ("lecture_02/homework2/tests/little_data.txt", "ü"),
    ],
)
def test_get_most_common_non_ascii_char(value: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(value)

    assert actual_result == expected_result
