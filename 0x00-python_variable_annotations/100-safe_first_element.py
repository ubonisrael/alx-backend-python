#!/usr/bin/env python3
"""Contains the type-annotated function safe_first_element"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    takes a list and returns the first element
    """
    if lst:
        return lst[0]
    else:
        return None
