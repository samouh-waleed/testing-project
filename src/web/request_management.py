from typing import Dict

def handle_request(request_data: Dict) -> Dict:
    """
    Simulate handling a web request. Possibly tested in integration tests.
    """
    method = request_data.get("method", "GET")
    if method == "GET":
        return {"status": "ok", "data": None}
    elif method == "POST":
        return {"status": "created", "data": request_data.get("payload")}
    else:
        return {"status": "error", "message": "Unsupported method"}

def parse_headers(headers: Dict) -> Dict:
    """
    Parse request headers. 
    Could be tested or partially tested in integration tests.
    """
    return {k.lower(): v for k, v in headers.items()}

def untested_request_logic():
    """
    Remains untested on purpose.
    """
    pass
