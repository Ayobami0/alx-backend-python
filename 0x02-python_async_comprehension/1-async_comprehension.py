#!/usr/bin/env python3
"""1. Async Comprehensions"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehensing.

    Return:
        List[float]: the comprehension.
    """
    lists: List[float] = [n async for n in async_generator()]

    return lists
