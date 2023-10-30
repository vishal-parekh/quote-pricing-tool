from faker import Faker
from factory.alchemy import SQLAlchemyModelFactory
from app.static_types.coverage import CoverageType
from app.static_types.state import State

from app.db.models import Quote
from app.db.setup import SessionLocal
from faker import Faker

fake = Faker()


# Quote factory with default values in case there are plans for future enhancement to make test suite more robust
class QuoteFactory(SQLAlchemyModelFactory):
    id = fake.unique.random_int(min=1, max=5)
    buyer_name = fake.name()

    buyer_state = fake.enum(State)
    coverage_type = fake.enum(CoverageType)
    has_pet = fake.pybool()
    requests_flood_coverage = fake.pybool()

    class Meta:
        model = Quote
        sqlalchemy_session = SessionLocal()
