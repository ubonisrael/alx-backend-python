#!/usr/bin/env python3
"""Contains the type-annotated function sum_list"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """
     takes a list input_list of floats
     as argument and returns their sum as a float
    """
    return reduce(lambda a, b: a + b, input_list)
