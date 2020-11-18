from unittest.mock import Mock, patch

import pytest

from lecture_04.homework4.tasks.task_2_mock_input import count_dots_on_i


@patch("urllib.request.urlopen")
def test_count_dots_on_i_positive(mock_obj):
    count_dots_on_i("https://example.com/")
    mock_obj.assert_called_with("https://example.com/")


def test_count_dots_on_i_negative():
    with pytest.raises(ValueError) as excinfo:
        mock = Mock()
        mock.side_effect = ValueError("Unreachable https://example2.om/")
        mock()

    assert "ValueError" in str(excinfo.type)
    assert "Unreachable https://example2.om/" in str(excinfo.value)
