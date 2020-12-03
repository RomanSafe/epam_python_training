from lecture_07.homework7.tasks.task3 import tic_tac_toe_checker


def test_tic_tac_toe_checker_x_wins():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]

    assert tic_tac_toe_checker(board) == "x wins!"


def test_tic_tac_toe_checker_0_wins():
    board = [
        ["o", "o", "o", "o"],
        ["-", "-", "-", "-"],
        ["-", "-", "x", "x"],
        ["x", "x", "x", "o"],
    ]

    assert tic_tac_toe_checker(board) == "o wins!"


def test_tic_tac_toe_checker_draw():
    board = [
        ["x", "o", "o", "o", "o"],
        ["x", "o", "x", "x", "x"],
        ["x", "o", "x", "x", "x"],
        ["x", "o", "x", "x", "x"],
        ["o", "x", "x", "x", "x"],
    ]

    assert tic_tac_toe_checker(board) == "draw!"


def test_tic_tac_toe_checker_unfinished():
    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

    assert tic_tac_toe_checker(board) == "unfinished!"
