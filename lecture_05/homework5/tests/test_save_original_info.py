import pytest

from lecture_05.homework5.tasks.save_original_info import custom_sum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
        ((1, 2, 3, 4), 10),
    ],
)
def test_custom_sum_decorated(capsys, value, expected_result):
    custom_sum(*value)
    without_print = custom_sum.__original_func
    captured = capsys.readouterr()

    assert str(expected_result) in captured.out
    assert custom_sum.__doc__ == custom_sum.__doc__
    assert custom_sum.__name__ == custom_sum.__name__
    # the result returns without printing
    assert without_print(*value) == expected_result
