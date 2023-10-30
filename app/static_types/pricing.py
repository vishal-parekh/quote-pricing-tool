from enum import Enum
from app.static_types.coverage import CoverageType
from app.static_types.state import State
from pydantic import BaseModel


class CoveragePriceFactors(Enum):
    FLOOD = "FLOOD"
    TAX = "TAX"


class FloodCoverageRate(float, Enum):
    CALIFORNIA = 0.02
    NEW_YORK = 0.1
    TEXAS = 0.5


class TaxRate(float, Enum):
    CALIFORNIA = 0.01
    NEW_YORK = 0.02
    TEXAS = 0.005


COVERAGE_TYPE_TO_FEE_MAPPING = {CoverageType.BASIC: 20.0, CoverageType.PREMIUM: 40.0}


class AddonCoverage(float, Enum):
    PET = 20.0


COVERAGE_BY_STATE_PRICE_MAPPING = {
    State.CALIFORNIA: {
        CoveragePriceFactors.FLOOD: FloodCoverageRate.CALIFORNIA,
        CoveragePriceFactors.TAX: TaxRate.CALIFORNIA,
    },
    State.NEW_YORK: {
        CoveragePriceFactors.FLOOD: FloodCoverageRate.NEW_YORK,
        CoveragePriceFactors.TAX: TaxRate.NEW_YORK,
    },
    State.TEXAS: {
        CoveragePriceFactors.FLOOD: FloodCoverageRate.TEXAS,
        CoveragePriceFactors.TAX: TaxRate.TEXAS,
    },
}


class QuotePrice(BaseModel):
    monthly_subtotal: float
    monthly_taxes: float
    monthly_total: float
