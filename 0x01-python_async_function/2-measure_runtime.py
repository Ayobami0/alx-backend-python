#!/usr/bin/env python3
"""2. Measure the runtime"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the time taken for a coroutine

    Param:
        n (int):  number of couritine
        max_delay (int):  max delay
    Return:
        float: the time taken
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop: float = time.time()

    t_time = stop - start

    return t_time / n
