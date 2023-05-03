#!/usr/bin/env python3
"""
Module for async generator task
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Coroutine that generates random float number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
