"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished!"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from collections import Counter
from collections.abc import Sequence
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks the state of the tic-tac-toe game.

    Args:
        board: list of lists filled with strings "-" - empty cell, "o" - steps of the
        first player, "x" - steps of the second player. This argument describes the
        state of a game at particular time moment. Amount of inner lists is the size of
        tic-tac-toe board.

    Returns:
        result of the check. It's one of the following strings: "x wins!", "o wins!",
        "draw!", "unfinished!".

    """

    board_size = len(board)
    results = set()

    def _check_state(tokens_sequence: Sequence) -> None:
        # Checks a state of the given row, column or diagonal (tokens_sequence).
        nonlocal results
        tokens_count = Counter(tokens_sequence)
        # If there are tokens of both players in current tokens_sequence,
        # nobody win. We don't keep information about draw, because
        # it is logically the last in the sequence of return statements.
        if "x" in tokens_count and "o" in tokens_count:
            pass
        # tokens_sequence ful of one player's tokens means he's won.
        elif tokens_count.get("x", None) == board_size:
            results.add("x")
        elif tokens_count.get("o", None) == board_size:
            results.add("o")
        # In other cases tokens_sequence is unfinished.
        else:
            results.add("u")

    diagonal_dec = []
    diagonal_inc = []
    for index, row in enumerate(board):
        _check_state(row)
        # Checks column. The number of column match to index.
        _check_state(next(zip(*board)))
        # Collects decreasing and increasing diagonals.
        diagonal_dec.append(row[index])
        diagonal_inc.append(row[-(index + 1)])

    _check_state(diagonal_dec)
    _check_state(diagonal_inc)

    if "x" in results:
        return "x wins!"
    elif "o" in results:
        return "o wins!"
    elif "u" in results:
        return "unfinished!"
    else:
        return "draw!"
