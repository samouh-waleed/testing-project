def fancy_math(x: float, y: float) -> float:
    """
    A formerly untested function with trivial logic 
    to let LLM generate test code.
    """
    # For example, sum then square for no real reason:
    return (x + y) ** 2

def fancy_print(msg: str) -> str:
    """
    Return the reversed string (and also print it) 
    so there's something to verify in a test.
    """
    reversed_msg = msg[::-1]
    print(reversed_msg)
    return reversed_msg
