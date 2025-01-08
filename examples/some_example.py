def demonstrate_nothing(param: int = 5) -> int:
    """
    Previously it just printed.
    Now we do a trivial multiply 
    and return it so the LLM can test.
    """
    val = param * 2
    print(f"Hello from some_example! param * 2 = {val}")
    return val
