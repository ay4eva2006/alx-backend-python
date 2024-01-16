#!/usr/bin/env python3
"""A Function to generate async generator using comprehension """
import asyncio
import random
from typing import Generator


sync def async_generator() -> Generator[float, None, None]:
    """A function that will loop 10 times, wait 1 sec. each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
