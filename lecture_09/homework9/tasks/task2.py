"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager
from typing import Iterator


class Suppressor:
    """Context manager, that suppresses passed exception.

    Attribute:
        exception_type: a name of exception to suppress.

    """

    def __init__(self, exception_type=None) -> None:
        """Initialises a class instance.

        Args:
            exception_type: a name of exception to suppress.

        """

        self.exception_type = exception_type

    def __enter__(self) -> None:
        pass

    def __exit__(self, *args) -> bool:
        """Exit the runtime context. The parameters describe the exception that caused
            the context to be exited.

        Returns:
            If an exception is supplied, it return True. Otherwise, the exception will
            be processed normally upon exit from this method.

        """

        return bool(self.exception_type)


@contextmanager
def suppressor(exception_type) -> Iterator:
    """Context manager, that suppresses passed exception.

    Args:
        exception_type: a name of exception to suppress.

    """

    try:
        yield
    except exception_type:
        pass
