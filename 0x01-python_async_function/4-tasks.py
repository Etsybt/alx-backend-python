#!/usr/bin/env python3
"""
Tasks and asyncio
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns a list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    delays = [await task for task in tasks]
    return delays
