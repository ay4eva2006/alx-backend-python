#!/usr/bin/env python3
from typing import Any
""" a python script that Safely returns the first element of an iterable or None if the iterable is empty.

    Parameters:
    - lst: The input iterable.

   Returns:
    - any: The first element of the iterable if it exists, otherwise None.
    """
def safe_first_element(lst) -> Any:
    if lst:
        return lst[0]
    else:
        return None
