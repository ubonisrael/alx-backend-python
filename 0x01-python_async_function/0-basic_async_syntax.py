#!/usr/bin/env python3
"""contains the wait_random coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes in an integer named max_delay and then waits
    for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
