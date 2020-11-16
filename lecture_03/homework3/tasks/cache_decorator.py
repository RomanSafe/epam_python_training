import functools
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

    def decorator_cache(function: Callable) -> Callable:
        container: dict = {}

        @functools.wraps(function)
        def wrapper_cache(*args, **kwargs) -> Any:
            repetitions = times
            if args or kwargs:
                cache_key = args + tuple(kwargs.items())
                if cache_key not in container:
                    container[cache_key] = function(*args, **kwargs)
                return container[cache_key]
            else:
                if (
                    function.__name__ in container
                    and container[function.__name__][1] > 0
                ):
                    container[function.__name__][1] -= 1
                    return container[function.__name__][0]
                container[function.__name__] = [function(), repetitions]
                return container[function.__name__][0]

        return wrapper_cache

    return decorator_cache
