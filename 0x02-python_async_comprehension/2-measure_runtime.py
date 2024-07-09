#!/usr/bin/env python3
"""
async func
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
     execute async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
