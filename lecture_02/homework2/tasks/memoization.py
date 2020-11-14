"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    """Accepts another function as an argument and return it with cach functionality.

    It means that a result of the first call of cached functin is saved in dictionary.
    The next calls with the same argument return result from dictionary without any
    evaluations.

    Args:
        func: function for caching.

    Returns:
        Function with cach functionality.

    """
    cache: dict = {}  # mypy demanded the type hint.

    def memoized_func(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result

    return memoized_func
