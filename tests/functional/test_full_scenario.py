import pytest
import asyncio
from src.data_processing.aggregator_utils import async_sum
from src.web.request_management import parse_headers
from src.web.response_management import add_cookie_to_response

@pytest.mark.asyncio
async def test_full_scenario_flow():
    """
    Functional test that uses async sum, parse_headers, and optionally add_cookie_to_response.
    """
    numbers = [10, 20, 30]
    total = await async_sum(numbers)
    assert total == 60

    headers = {"Content-Type": "application/json", "User-Agent": "TestRunner"}
    parsed = parse_headers(headers)
    assert "content-type" in parsed
    assert "user-agent" in parsed

    # We'll test add_cookie_to_response here
    resp = {"status_code": 200, "headers": {}, "body": "OK"}
    updated_resp = add_cookie_to_response(resp, "session_id", "abc123")
    assert "Set-Cookie" in updated_resp
    assert updated_resp["Set-Cookie"][0] == "session_id=abc123"

    # Not calling e.g. build_response directly, so coverage on that might remain partial.
