#!/usr/bin/env python3
""" A python script to annonate a TypeVar"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """function to return a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
