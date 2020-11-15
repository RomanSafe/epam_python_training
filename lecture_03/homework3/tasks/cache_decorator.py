from collections.abc import Callable
from typing import Any


def cache(times: int) -> Callable:
    """Remembers other function output value. Gives out cached value up to "times"
    number only.

    Args:
        times: quantity of returned cached values.

    Returns:
        Wrapper around recieved functon with cache functionality.

    """
    def wrapper(function: Callable) -> Callable:
        container: dict = {}

        def substitute() -> Any:
            repetitions = times
            if function in container and container[function][1] > 0:
                container[function][1] -= 1
                return container[function][0]
            container[function] = [function(), repetitions]
            return container[function][0]
        return substitute
    return wrapper
