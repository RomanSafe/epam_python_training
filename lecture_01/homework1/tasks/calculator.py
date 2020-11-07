def check_power_of_2(number: int) -> bool:
    """This function checks if given argument represents power of 2.

    Args:
        number: single argument.

    Returns:
        If number represents power of 2 - True, owervise False.
    """
    return (number != 0) and ((number & (number - 1)) == 0)
