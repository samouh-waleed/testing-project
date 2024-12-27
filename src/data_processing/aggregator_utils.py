from typing import List
import asyncio

async def async_square(x: float) -> float:
    """
    Asynchronously squares a number.
    Possibly tested in test_aggregator_utils.
    """
    return x * x

async def async_sum(numbers: List[float]) -> float:
    """
    Asynchronously sums numbers.
    Possibly tested. Or left partially tested.
    """
    return sum(numbers)

def sync_difference(a: float, b: float) -> float:
    """
    Simple synchronous difference.
    This is tested in test_aggregator_utils.
    """
    return a - b

def never_used_aggregator_util():
    """
    Function never used or tested, remains untested.
    """
    return "unused"
