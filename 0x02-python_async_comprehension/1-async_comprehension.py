#!/usr/bin/env python3
"""A function that generate async generator"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine that collect 10 ramdom numbers(return floats type list) using async comprehension"""
    results = [i async for i in async_generator()]
    return results
