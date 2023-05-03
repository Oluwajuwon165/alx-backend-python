#!/usr/bin/env python3
"""
An async generator that yields 10 random numbers between 0 and 10
with a delay of 1 second between each iteration.
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Coroutine that generates 10 random numbers between 0 and 10
    with a delay of 1 second between each iteration.

    Yields:
        float: a random float between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
