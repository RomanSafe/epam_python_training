from lecture_04.homework4.tasks.task_3_get_print_output import my_precious_logger


def test_my_precious_logger(capsys):
    my_precious_logger("OK\n")
    my_precious_logger("error: file not found\n")
    captured = capsys.readouterr()  # CaptureResult(out='', err='')
    # Не порял почему пустые атрибуты. Пробовал менять настойки Capture - не помогло.
    # Тестовый текст печатает в stdout и stderr соответственно.
    # Работают команды из тестовой функции, а внешние нет.

    assert captured.out == "OK\n"
    assert captured.err == "error: file not found\n"
