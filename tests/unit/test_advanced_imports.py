import pytest
from src.core.advanced_imports import dynamic_import, dynamic_import_from_string

def test_dynamic_import_valid():
    math_module = dynamic_import("math")
    assert math_module is not None
    assert hasattr(math_module, "sin")

def test_dynamic_import_invalid():
    assert dynamic_import("non_existent_stuff") is None

def test_dynamic_import_from_string():
    sin_func = dynamic_import_from_string("math.sin")
    assert sin_func is not None
    assert callable(sin_func)

# never_tested_function remains untested.
