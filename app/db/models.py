from sqlalchemy import Boolean, Column, Enum, Integer, String

from app.static_types.coverage import CoverageType
from app.static_types.state import State
from app.db.setup import Base


class Quote(Base):
    __tablename__ = "quotes"

    # The system could utilize uuid field type for the PK but for this task/feature set,
    # integer type will be used for simplicity, easier readability, and sequential record organization
    id = Column(Integer, primary_key=True)
    buyer_name = Column(String, nullable=False)
    buyer_state = Column(Enum(State), nullable=False, name="buyer_state")
    coverage_type = Column(Enum(CoverageType), nullable=False, name="coverage_type")
    has_pet = Column(Boolean, default=False)
    requests_flood_coverage = Column(Boolean, default=False)
