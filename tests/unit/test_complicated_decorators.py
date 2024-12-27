import pytest
from src.core.complicated_decorators import debug_decorator

@debug_decorator
def sample_function(x, y):
    return x + y

def test_debug_decorator():
    result = sample_function(2, 3)
    assert result == 5

# We do not test untested_decorator, 
# so it remains uncovered.
