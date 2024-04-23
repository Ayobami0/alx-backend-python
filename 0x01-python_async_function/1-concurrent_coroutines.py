#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay

    Param:
        n (int): number of times
        max_delay (int): maximum delay
    Return:
        List[float]: list of the delays redurned by wait_random
    """
    return sorted(await asyncio.gather(*[wait_random(max_delay) for _ in range(n)]))
