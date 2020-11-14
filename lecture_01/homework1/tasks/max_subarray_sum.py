"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16

"""
from collections import deque
from typing import Deque, List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Looks for a sub-array with length less then or equal to "k",
    with maximal sum.

    Args:
        nums: array of numbers where the function looks for.
        k: sub-array length limit.

    Returns:
        maximal sum.

    """
    sub_array: Deque = deque((), k)
    maximum_sum = nums[0]
    sub_array_sum = 0
    for number in nums:
        sub_array.append(number)
        sub_array_sum = sum(sub_array)
        maximum_sum = max(maximum_sum, sub_array_sum)
        for number_ in tuple(sub_array)[:-1]:
            part_of_sub_array_sum = sub_array_sum - number_
            maximum_sum = max(maximum_sum, part_of_sub_array_sum)
            sub_array_sum = part_of_sub_array_sum
    return maximum_sum
