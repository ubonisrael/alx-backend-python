#!/usr/bin/env python3
"""Contains the type-annotated function sum_mixed_list"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    return reduce(lambda a, b: a + b, mxd_list)
