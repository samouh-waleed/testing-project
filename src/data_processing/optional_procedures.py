from typing import List, Optional

def maybe_reverse_list(items: List[int], do_reverse: bool = False) -> List[int]:
    """
    If do_reverse=True, reverse the list. 
    Partially tested, e.g., tested with do_reverse=True but not with do_reverse=False.
    """
    if do_reverse:
        return list(reversed(items))
    return items

def optional_sum(items: Optional[List[int]] = None) -> int:
    """
    Sum items if not None, else return 0.
    Possibly tested or missed in test_optional_procedures.
    """
    if items is None:
        return 0
    return sum(items)

def untested_optional_func(val: int = 10) -> str:
    """
    Never called or tested.
    Now does trivial logic for the LLM to test.
    """
    if val > 5:
        return "Value is above 5"
    else:
        return "Value is 5 or below"
