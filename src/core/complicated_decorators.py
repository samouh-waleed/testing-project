from functools import wraps
from typing import Callable

def debug_decorator(func: Callable) -> Callable:
    """
    A simple decorator to debug function calls.
    This is tested in test_complicated_decorators.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result}")
        return result
    return wrapper

def untested_decorator(func: Callable) -> Callable:
    """
    We never test or use this decorator, so it remains untested.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("This is the untested decorator in action!")
        return func(*args, **kwargs)
    return wrapper
