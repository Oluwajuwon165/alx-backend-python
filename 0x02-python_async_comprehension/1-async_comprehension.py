#!/usr/bin/env python3
"""
An async comprehension that collects 10 random numbers from async_generator.
"""

from typing import List

from asyncio import gather

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator using an
    async comprehension.

    Returns:
        List[float]: a list of 10 random floats between 0 and 10
    """
    return [x async for x in async_generator()][:10]
