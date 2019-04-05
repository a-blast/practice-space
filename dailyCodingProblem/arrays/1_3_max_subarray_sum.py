# -*- encoding: utf-8 -*-
"""Get maximum subarray sum"""
from typing import List
from itertools import accumulate


def get_max_subarray_sum(arr: List[int]) -> int:
    """Get the maximum sum that can be found from a contiguous sub array."""
    max_so_far, max_ending_here = (0, 0)
    for entry in arr:
        max_ending_here = max(entry, max_ending_here + entry)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def get_max_subarray_sum_funtional(arr: List[int]) -> int:
    max_so_far = accumulate(arr, lambda val1, val2: max(val1 + val2, val2))
    return max(max_so_far)
