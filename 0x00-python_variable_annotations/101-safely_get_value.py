#!/usr/bin/env python3
"""Contains the type-annotated function safely_get_value"""
from typing import Mapping, Union, Any, TypeVar
from types import NoneType

T = TypeVar("T")
Tvar = Union[T, NoneType]
Dvar = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Tvar = None) -> Dvar:
    """safely returns a value"""
    if key in dct:
        return dct[key]
    else:
        return default
