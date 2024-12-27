import pytest
from src.data_processing.optional_procedures import maybe_reverse_list, optional_sum

def test_maybe_reverse_list_true():
    data = [1, 2, 3]
    reversed_data = maybe_reverse_list(data, do_reverse=True)
    assert reversed_data == [3, 2, 1]

# We do NOT test do_reverse=False, leaving partial coverage
# for maybe_reverse_list.

def test_optional_sum():
    assert optional_sum([1, 2, 3]) == 6

# We do not test optional_sum(None) or untested_optional_func.
