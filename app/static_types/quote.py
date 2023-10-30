from pydantic import BaseModel
from .state import State
from .coverage import CoverageType


class Quote(BaseModel):
    id: int
    buyer_name: str
    buyer_state: State
    coverage_type: CoverageType
    has_pet: bool
    requests_flood_coverage: bool
