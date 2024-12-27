import pytest
import asyncio
from src.data_processing.aggregator_utils import async_square, sync_difference

@pytest.mark.asyncio
async def test_async_square():
    result = await async_square(5)
    assert result == 25

def test_sync_difference():
    assert sync_difference(10, 3) == 7

# We do not test async_sum or never_used_aggregator_util, 
# so coverage is partial for aggregator_utils.
