from string import ascii_lowercase
from typing import Any, List, Sequence, Tuple

import pytest

from lecture_02.homework2.tasks.custom_range import get_custom_range


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        ((ascii_lowercase, "g", "p"), ["g", "h", "i", "j", "k", "l", "m", "n", "o"]),
        ((ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
    ],
)
def test_get_custom_range(value: Tuple[Sequence[Any]], expected_result: List[Any]):
    actual_result = get_custom_range(*value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_exception", "expected_message"],
    [
        (
            (ascii_lowercase, "p", "g", -2, 7),
            Exception,
            "Amonunt of range parameters is exceeded. Maximum is 3.",
        ),
    ],
)
def test_get_custom_range_v2(
    value: Tuple[Sequence[Any]], expected_exception: Exception, expected_message: str
):
    """Test for exception."""
    with pytest.raises(Exception) as exc_info:
        get_custom_range(*value)

    assert exc_info.type is expected_exception
    assert exc_info.value.args[0] == expected_message
