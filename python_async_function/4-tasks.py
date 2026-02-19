#!/usr/bin/env python3
"""
new function task_wait_n. The code is nearly identical to wait_n
except task_wait_random is being called.
"""


from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Execute task_wait_random and return sorted list of delay"""
    tasks = [task_wait_random(max_delay) for _ in rang(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        reslut = await task
        delays.append(result)
        
        return delays
