import pytest

from lecture_03.homework3.tasks.filter import Filter, make_filter, sample_data


@pytest.mark.parametrize(
    ["functions", "test_data"],
    [
        (
            [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)],
            range(0, 100),
        ),
    ],
)
def test_filter_apply(functions, test_data):
    filter = Filter(functions)
    positive_even = filter.apply(test_data)

    assert positive_even == [item for item in range(2, 100) if item % 2 == 0]


@pytest.mark.parametrize(
    ["specified_keywords", "test_data", "expected_result"],
    [
        (
            {"name": "polly", "type": "bird"},
            sample_data,
            [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}],
        ),
    ],
)
def test_make_filter(specified_keywords, test_data, expected_result):
    result = make_filter(name="polly", type="bird").apply(sample_data)

    assert result == expected_result
