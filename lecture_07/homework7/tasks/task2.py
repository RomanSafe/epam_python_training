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

    first_index = len(first) - 1
    second_index = len(second) - 1
    skip_in_first = 0
    skip_in_second = 0
    while first_index >= 0 or second_index >= 0:
        # In the next two blocks we correct words, if there are "#" or what to skip.
        if first[first_index] == "#":
            skip_in_first += 1
            first_index -= 1
            continue
        elif skip_in_first > 0:
            first_index -= 1
            skip_in_first -= 1
            continue

        if second[second_index] == "#":
            skip_in_second += 1
            second_index -= 1
            continue
        elif skip_in_second > 0:
            second_index -= 1
            skip_in_second -= 1
            continue
        # Here we check if there are letters in one string and another one is empty.
        if (
            first_index >= 0
            and second_index < 0
            or first_index < 0
            and second_index >= 0
        ):
            return False

        if first[first_index] != second[second_index]:
            return False
        first_index -= 1
        second_index -= 1
    return True
