#!/usr/bin/env python3
"""Contains the type-annotated function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes a list and returns a list containing tuples with the elements
    and their corresponding length
    """
    return [(i, len(i)) for i in lst]
