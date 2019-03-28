# -*- coding: utf-8 -*-

"""
Get product of all other elements.

Map an array into a new array where each element is the
product of all elements but itself.
"""

from functools import reduce, accumulate
import operator

def solution1(array):
    """Array product transformation with division"""
    product = reduce(operator.mul, array)
    out = [product/val for val in array]
    return out

def solution2(array):
    """Implement without division"""
    prefix_products = accumulate(array, operator.mul)
    suffix_products = reversed(list(accumulate(reversed(array), operator.mul)))

    prefix_products = list(prefix_products)
    suffix_products = list(suffix_products)

    out = []

    for index in range(len(array)):
        if index == 0:
            out.append(suffix_products[index+1])
        elif index == len(array)-1:
            out.append(prefix_products[index-1])
        else:
            out.append(
                prefix_products[index-1] * suffix_products[index+1],
            )

    return out
