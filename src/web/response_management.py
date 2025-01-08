from typing import Dict
import json

def build_response(body: Dict, status_code: int = 200) -> Dict:
    """
    Build a JSON-like response object. Possibly tested in test_integration_flow or test_full_scenario.
    """
    return {
        "status_code": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def add_cookie_to_response(response: Dict, cookie_name: str, cookie_value: str) -> Dict:
    """
    Potentially tested or left out.
    """
    if "Set-Cookie" not in response:
        response["Set-Cookie"] = []
    response["Set-Cookie"].append(f"{cookie_name}={cookie_value}")
    return response

def never_used_response_helper(x: int) -> Dict:
    """
    Not tested, ensuring untested coverage path.
    Now it has trivial logic for the LLM to test.
    """
    return {"msg": f"Response helper saw {x}"}
