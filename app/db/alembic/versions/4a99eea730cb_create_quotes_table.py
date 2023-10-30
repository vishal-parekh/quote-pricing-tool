"""create quotes table

Revision ID: 4a99eea730cb
Revises: 
Create Date: 2023-10-11 10:58:59.412046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "4a99eea730cb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create quotes table with necessary columns and appropriate types using Alembic
    quotes_table = op.create_table(
        "quotes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("buyer_name", sa.String(50), nullable=False),
        sa.Column(
            "buyer_state",
            sa.Enum("CALIFORNIA", "NEW_YORK", "TEXAS", name="state"),
            nullable=False,
        ),
        sa.Column(
            "coverage_type",
            sa.Enum("BASIC", "PREMIUM", name="coverage_type"),
            nullable=False,
        ),
        sa.Column("has_pet", sa.Boolean, default=False, nullable=False),
        sa.Column("requests_flood_coverage", sa.Boolean, default=False, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    # Seed quotes table with test data from assignment instructions
    op.bulk_insert(
        quotes_table,
        [
            {
                "id": 1,
                "buyer_name": "Quote Test Case 1",
                "buyer_state": "CALIFORNIA",
                "coverage_type": "BASIC",
                "has_pet": True,
                "requests_flood_coverage": True,
            },
            {
                "id": 2,
                "buyer_name": "Quote Test Case 2",
                "buyer_state": "CALIFORNIA",
                "coverage_type": "PREMIUM",
                "has_pet": True,
                "requests_flood_coverage": True,
            },
            {
                "id": 3,
                "buyer_name": "Quote Test Case 3",
                "buyer_state": "NEW_YORK",
                "coverage_type": "PREMIUM",
                "has_pet": True,
                "requests_flood_coverage": False,
            },
            {
                "id": 4,
                "buyer_name": "Quote Test Case 4",
                "buyer_state": "TEXAS",
                "coverage_type": "BASIC",
                "has_pet": False,
                "requests_flood_coverage": True,
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("quotes")
