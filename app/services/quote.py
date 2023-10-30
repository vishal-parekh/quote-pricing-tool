from app.db.models import Quote

from sqlalchemy import exc
import logging as log
from app.static_types.pricing import (
    COVERAGE_TYPE_TO_FEE_MAPPING,
    COVERAGE_BY_STATE_PRICE_MAPPING,
    CoveragePriceFactors,
    QuotePrice,
    AddonCoverage,
)
from app.static_types.pricing import QuotePrice
from app.db.setup import Session


class QuoteService:
    @staticmethod
    def get_quote(quote_id: int) -> Quote:
        try:
            return Session.query(Quote).get(quote_id)
        except exc.SQLAlchemyError as e:
            log.exception(f"QuoteService.get_quote.error: {e}")
            raise e

    @classmethod
    def calculate_quote_price(cls, quote_id: int) -> QuotePrice:
        # Get quote details using quote_id parameter when making call to static class method
        quote_request_payload: Quote = QuoteService.get_quote(quote_id)

        # Retrieve base price based on requested quote coverage type
        base_price = COVERAGE_TYPE_TO_FEE_MAPPING[quote_request_payload.coverage_type]

        # If determined as true from requested quote details, add cost for miscallaneous coverage options and add to base price
        if quote_request_payload.has_pet:  # if has_pet
            base_price += AddonCoverage.PET

        if quote_request_payload.requests_flood_coverage:  # if wants_flood_coverage
            base_price += (
                base_price
                * COVERAGE_BY_STATE_PRICE_MAPPING[quote_request_payload.buyer_state][
                    CoveragePriceFactors.FLOOD
                ]
            )

        subtotal = base_price
        # Calculate taxes based on buyer's residential state and multiply it by subtotal
        taxes = (
            subtotal
            * COVERAGE_BY_STATE_PRICE_MAPPING[quote_request_payload.buyer_state][
                CoveragePriceFactors.TAX
            ]
        )
        # Calculate grand total by finding the sum of the subtotal and tax amount
        total = subtotal + taxes

        return QuotePrice(
            monthly_subtotal=subtotal,
            monthly_taxes=taxes,
            monthly_total=total,
        )
