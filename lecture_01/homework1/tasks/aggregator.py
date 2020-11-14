"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l]
is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.

"""
from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Takes four lists of integer values as arguments,
    compute how many tuples (i, j, k, l) there are such that a[i] + b[j] + c[k] + d[l]
    is zero. Items with different and equel indexes are counted.

    Args:
        a, b, c, d have same length of N where 0 ≤ N ≤ 1000.

    Returns:
        amount of found tuples with sum of items is zero.

    """
    result = 0
    for item in product(a, b, c, d):
        if sum(item) == 0:
            result += 1
    return result
