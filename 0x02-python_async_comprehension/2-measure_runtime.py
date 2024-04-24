#!/usr/bin/env python3

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of async gather and return it.

    Return:
        float: the total runtime
    """
    start: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop: float = time.time()

    return stop - start
