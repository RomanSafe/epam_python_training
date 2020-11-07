import pytest
from calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (65536, True),
        (12, False),
        (1, True),
        (4, True),
        (3, False),
        (72862937287, False),
        (-1, False),
        (-4, False),
        (-200000000000, False),
        (-65536, False),
        (68719476736, True),
        (0, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
