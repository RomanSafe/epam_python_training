def check_power_of_2(number: int) -> bool:
    """Checks if given argument represents power of 2.

    Args:
        number: is checked for power of 2.

    Returns:
        If number represents power of 2 - True, owervise False.

    """
    return (number != 0) and ((number & (number - 1)) == 0)
