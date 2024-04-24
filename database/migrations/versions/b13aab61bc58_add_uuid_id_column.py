"""Add uuid_id column

Revision ID: b13aab61bc58
Revises: eac96f6f0138
Create Date: 2024-04-24 14:27:59.955545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b13aab61bc58'
down_revision: Union[str, None] = 'eac96f6f0138'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uuid_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'uuid_id')
    # ### end Alembic commands ###