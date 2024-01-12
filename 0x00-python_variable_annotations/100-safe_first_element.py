#!/usr/bin/env python3
from typing import Sequence, Any, Union, Optional
""" a python script that Safely returns the first element of an iterable or None if the iters, otherwise None."""

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
