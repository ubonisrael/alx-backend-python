#!/usr/bin/env python3
"""Contains the type-annotated function safely_get_value"""
from typing import Mapping, Union, Any, TypeVar
from types import NoneType

T = TypeVar("T")
def safely_get_value(dct: Mapping, key: Any, default: Union[T, NoneType] = None) -> Union[Any, T]:
    """safetly returns a value"""
    if key in dct:
        return dct[key]
    else:
        return default