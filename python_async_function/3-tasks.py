#!/usr/bin/env python3
"""
3-tasks module
Creates and returns an asyncio.Task for wait_random coroutine.
"""

import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): maximum delay in seconds

    Returns:
        asyncio.Task: scheduled task
    """
    return asyncio.create_task(wait_random(max_delay))
