from app.tests.factory.quote_factory import QuoteFactory
from app.static_types.coverage import CoverageType
from app.static_types.state import State
from app.services.quote import QuoteService
from app.db.models import Quote


# Test case using QuoteFactory as mock to test against application database-stored quote record.
# TODO: Create test database instance with mock seed data and to be able to setup, teardown, and manipulate data for multiple, robust test suite.
def test_get_quote_success():
    # Use the factory to create a quote instance
    quote = QuoteFactory(
        id=1,
        buyer_name="Quote Test Case 1",
        buyer_state=State.CALIFORNIA,
        coverage_type=CoverageType.BASIC,
        has_pet=True,
        requests_flood_coverage=True,
    )

    # Call service class method to get quote
    quote_response: Quote = QuoteService.get_quote(1)

    assert quote_response is not None
    assert quote_response.id == quote.id
    assert quote_response.buyer_name == quote.buyer_name
    assert quote_response.buyer_state == quote.buyer_state
    assert quote_response.coverage_type == quote.coverage_type
    assert quote_response.requests_flood_coverage == quote.requests_flood_coverage
