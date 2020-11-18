from unittest.mock import Mock, patch

import pytest

from lecture_04.homework4.tasks.task_2_mock_input import count_dots_on_i


@patch("requests.get")
def test_count_dots_on_i_positive(mock_obj):
    mock_obj.return_value = Mock(text="<div>ia ia ia</div> should == 5")
    result = count_dots_on_i("https://example.com/")

    mock_obj.assert_called_with("https://example.com/")
    assert result == 5


def test_count_dots_on_i_negative():
    with pytest.raises(ValueError) as exc_info:
        mock = Mock()
        mock.side_effect = ValueError("Unreachable https://example2.om/")
        mock()

    assert "ValueError" in str(exc_info.type)
    assert "Unreachable https://example2.om/" in str(exc_info.value)
