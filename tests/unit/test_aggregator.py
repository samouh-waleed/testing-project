import pytest
from src.data_processing.aggregator import aggregate_numbers

def test_aggregate_numbers_basic():
    assert aggregate_numbers([1, 2, 3]) == 6

def test_aggregate_numbers_empty():
    assert aggregate_numbers([]) == 0

# We do NOT test product_of_numbers or never_called_aggregator_function in this file,
# ensuring they remain partially or fully untested.
