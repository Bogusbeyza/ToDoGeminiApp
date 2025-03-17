"""phone number added

Revision ID: f09498a70c97
Revises: 
Create Date: 2025-03-12 01:28:29.138460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f09498a70c97'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number',sa.String(), nullable=True))


def downgrade() -> None:
    #op.drop_column("users", "phone_number" )
    pass
