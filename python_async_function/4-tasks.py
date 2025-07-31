#!/usr/bin/env python3
"""
4-tasks module
Spawns task_wait_random n times and returns delays in order of completion.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with max_delay.

    Returns:
        List[float]: list of delays, in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        results.append(result)
    return results
