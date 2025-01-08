from typing import List
import math

def aggregate_numbers(numbers: List[float]) -> float:
    """
    Sums up the list of numbers. 
    This is tested by test_aggregator.py (fully tested).
    """
    return sum(numbers)

def product_of_numbers(numbers: List[float]) -> float:
    """
    Returns the product of all numbers. 
    This is partially tested or possibly not tested at all if tests do not call it.
    """
    prod = 1
    for n in numbers:
        prod *= n
    return prod

def geometric_mean(numbers: List[float]) -> float:
    """
    Example function that might be tested in one scenario but not in others.
    We'll assume it's tested partially in test_integration_flow.
    """
    if not numbers:
        return 0.0
    prod = product_of_numbers(numbers)
    return math.pow(prod, 1.0 / len(numbers))

def never_called_aggregator_function(x: float, y: float) -> float:
    """
    We never test or call this aggregator function, 
    ensuring it's untested.
    Now it does trivial logic:
    """
    return x**2 + y**2
