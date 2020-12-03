"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str) -> bool:
    """Edits two given strings and compare them.

    Args:
        first: string for correction and comparison;
        second: string for correction and comparison.

    Returns:
        True if both edited arguments are equal, otherwise False.

    """

    def _edit_string(text: str):
        # Does backspace operations on the given text
        edited_text: list = []
        for letter in text:
            if edited_text and letter == "#":
                edited_text.pop()
            else:
                edited_text.append(letter)
        return edited_text

    return _edit_string(first) == _edit_string(second)
