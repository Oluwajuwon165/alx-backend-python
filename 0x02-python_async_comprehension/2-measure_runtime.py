#!/usr/bin/env python3
"""
A coroutine that measures the total runtime of four parallel
async comprehensions using asyncio.gather().
"""

import time
from typing import List

from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of four parallel
    async comprehensions using asyncio.gather().

    Returns:
        float: the total runtime in seconds
    """
    start_time = time.perf_counter()

    await gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter2-measure_runtime.py()

    return end_time - start_time
