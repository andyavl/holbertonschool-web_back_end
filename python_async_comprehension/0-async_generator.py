#!/usr/bin/env python3
"""
0-async_generator module
Yields random numbers between 0 and 10, with 1 second delay, 10 times.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random float between 0 and 10,
    10 times with a 1-second wait between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
