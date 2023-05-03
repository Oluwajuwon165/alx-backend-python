#!/usr/bin/env python3
"""Module with an asynchronous generator that yields random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """Asynchronous generator that yields random numbers."""
    for Jhay in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
