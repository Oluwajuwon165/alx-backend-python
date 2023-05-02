#!/usr/bin/env python3
"""Regular function syntax to create a Task"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a asyncio.Task that waits for a random delay"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
