import pytest
from src.data_processing.aggregator import geometric_mean
from src.web.request_management import handle_request
from src.web.response_management import build_response

@pytest.mark.integration
def test_integration_geometric_mean_and_request():
    """
    Tests partial integration: calls geometric_mean, handle_request, build_response.
    """
    nums = [1, 2, 3, 4]
    gm = geometric_mean(nums)
    assert gm > 2.0

    req = {"method": "POST", "payload": {"hello": "world"}}
    response_dict = handle_request(req)
    assert response_dict["status"] == "created"

    final = build_response(response_dict, status_code=201)
    assert final["status_code"] == 201

# Not covering product_of_numbers or add_cookie_to_response, etc.
