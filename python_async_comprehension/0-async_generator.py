#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments.
"""


from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generator that yield a random value"""
    for i in range(10):
        await sleep(1)
        yield 10 * random()
