#!/usr/bin/env python3
""" a python script to annonate any type"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function to return a any or None type"""
    if lst:
        return lst[0]
    else:
        return None
