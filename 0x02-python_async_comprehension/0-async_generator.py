#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loop 10 times, wait 1 sec each time"""
    await asyncio.sleep(0)  # Allow event loop to switch tasks
    return (random.uniform(0, 10) for _ in range(10))
