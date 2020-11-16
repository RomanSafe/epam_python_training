import hashlib
import random
import struct
import time
from collections.abc import Callable, Iterable
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_sum(function: Callable, iterable: Iterable, processes: int = 501) -> int:
    """Calculates total sum of slow_calculate() of all numbers starting from 0 to 500
    (last included). Used functional capabilities of multiprocessing module.

    Args:
        function: for using in map().
        iterable: to iterate through.
        processes: is the number of worker processes to use. Defaults to 501.

    Returns:
        total sum of slow_calculate() of all numbers starting from 0 to 500.

    """
    with Pool(processes) as p:
        result = sum(p.map(function, iterable))
    return result
