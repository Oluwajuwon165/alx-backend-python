#!/usr/bin/env python3
"""
The basics of async - Task 1
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Return:
        A list of all the delays (float values) in ascending order.
    """
    delays = []
    tasks = []

    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
