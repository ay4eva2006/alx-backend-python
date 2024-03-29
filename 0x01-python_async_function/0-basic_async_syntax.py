#!/usr/bin/env python3
""" A function to create async and await"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ a function to create asynchronous coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
