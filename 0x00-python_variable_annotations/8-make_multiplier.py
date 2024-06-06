#!/usr/bin/env python3
"""Contains the type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and returns a
    function that multiplies a float by multiplier
    """
    return lambda a: a * multiplier
