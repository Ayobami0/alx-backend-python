#!/usr/bin/env python3
"""0. The basics of async"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and
    max_delay seconds and eventually returns it.

    Param:
        max_delay (int): the maximum delay to wait for
    Return:
        Coroutine: The couritine
    """
    delay: float = uniform(0, max_delay)

    await asyncio.sleep(delay)
    return delay
