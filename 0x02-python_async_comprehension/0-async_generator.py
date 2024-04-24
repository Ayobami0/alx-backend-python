#!/usr/bin/env python3
"""0. Async Generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random number for each loop.

    Return:
        Genetrator[int, None, None]
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
