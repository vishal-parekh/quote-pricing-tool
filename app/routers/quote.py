from fastapi import APIRouter, HTTPException
from app.static_types.pricing import QuotePrice
from app.services.quote import QuoteService
import logging as log

router = APIRouter()


# Pricing logic is built out and defined in service class method to perform calculation and is called and returned here.
@router.get("/price/quote_id/{quote_id}", response_model=QuotePrice)
def get_quote_price(quote_id: int):
    try:
        return QuoteService.calculate_quote_price(quote_id)
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        log.exception(f"api.routers.quote.get_quote_price.error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
