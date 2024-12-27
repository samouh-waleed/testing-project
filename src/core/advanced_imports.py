import importlib
from typing import Any, Optional

def dynamic_import(module_name: str) -> Optional[Any]:
    """
    Dynamically import a module.
    This function is tested partially: we test some valid imports, but not all error cases.
    """
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None

def dynamic_import_from_string(import_string: str) -> Optional[Any]:
    """
    Import an attribute from a fully qualified string e.g. 'math.sin'
    This is tested in test_advanced_imports but not for all edge cases.
    """
    try:
        module_name, attr_name = import_string.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, attr_name)
    except (ImportError, AttributeError):
        return None

def never_tested_function():
    """
    We never call or test this function,
    so it should remain untested.
    """
    print("I'm never tested and never called!")
