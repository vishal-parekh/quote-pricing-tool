from unittest import mock
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.static_types.pricing import QuotePrice
from app.tests.mocks.get_quote_price_response import quote_price_responses

client = TestClient(app)


# Test case that parameterizes existing quotes (via quote_id) in database generated and seeded on setup. Router endpoint responses tested against responses defined in mocks
# Test cases for routers can be enhanced by testing exception handling using pytest.raises()
@pytest.mark.parametrize("quote_id_param", [1, 2, 3, 4])
def test_get_quote_price_success(quote_id_param: int):
    mock_responses = mock.MagicMock()
    mock_responses.side_effect = quote_price_responses

    with mock.patch("app.routers.quote.get_quote_price", mock_responses):
        response = client.get(f"/price/quote_id/{quote_id_param}")

        assert response.status_code == 200
        response_json = response.json()

        quote_response = QuotePrice(**response_json)
        assert quote_response is not None
