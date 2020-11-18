from lecture_04.homework4.tasks.task_3_get_print_output import my_precious_logger


def test_my_precious_logger(capsys):
    my_precious_logger("OK")
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()

    assert "OK" in captured.out
    assert "error: file not found" in captured.err
