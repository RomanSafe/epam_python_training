"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func

print_result изменять нельзя, за исключением добавления вашего
декоратора на место отведенное под него

До применения вашего декоратор будет вызываться AttributeError при
custom_sum.__original_func . Это корректное поведение.
После применения там должна быть исходная функция.

Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>

"""
import functools
from collections.abc import Callable


def save_func_and_its_meta(func: Callable) -> Callable:
    """Decorator for a wrapper function.

    Updates a wrapper function to look like the wrapped function (func).

    To use:
        add decorator @save_func_and_its_meta(func) before the wrapper
        function declatation.

    Args:
        func: original function that we want to save.

    Returns:
        inner function that saves __name__ and __doc__ attributes of recieved func's
        and func itself.

    """

    def inner(wrapper: Callable) -> Callable:
        """Saves attributes __name__ and __doc__ of recieved func, saves this func in the
        attribute __original_func of the wrapper function.

        Args:
            wrapper: the decorated wrapper function.

        Returns:
            wrapper function with changed attributes.

        """
        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        wrapper.__original_func = func  # type: ignore
        return wrapper

    return inner


def print_result(func):
    @save_func_and_its_meta(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func

    # the result returns without printing
    print(without_print(1, 2, 3, 4) == 10)
