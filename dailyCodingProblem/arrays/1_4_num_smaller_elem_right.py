# -*- coding: utf-8 _-*-
"""
Calculates the number of smaller elements to the right of every element
in an array
"""

from typing import List
import bisect


def smaller_counts(arr: List[int]) -> List[int]:
