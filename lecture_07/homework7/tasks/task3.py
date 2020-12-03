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
from typing import List, Optional


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

    def _check_state(tokens_sequence: list) -> Optional[str]:
        # Checks a state of the given tokens_sequence.
        nonlocal results
        state_checker = Counter(tokens_sequence)
        if "x" in state_checker and "o" in state_checker:
            results.add("draw!")
            return None
        elif "x" in state_checker and state_checker["x"] == board_size:
            return "x wins!"
        elif "o" in state_checker and state_checker["o"] == board_size:
            return "o wins!"
        else:
            results.add("unfinished!")
            return None

    diagonal_dec = []
    diagonal_inc = []
    for index, row in enumerate(board):
        diagonal_dec.append(row[index])
        # backward index count to collect increasing diagonal
        diagonal_inc.append(row[-(index + 1)])
        winner = _check_state(row)
        if winner:
            return winner
    for column in zip(*board):
        winner = _check_state(column)
        if winner:
            return winner
    return "unfinished!" if "unfinished!" in results else "draw!"
