#!/usr/bin/env python3
"""3. Tasks"""

import asyncio
from asyncio.tasks import Task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """Waits for a random delay between 0 and max_delay
    seconds and eventually returns it.

    Param:
        max_delay (int): the maximum delay to wait for
    Return:
        Coroutine: The couritine
    """
    return asyncio.create_task(wait_random(max_delay))
