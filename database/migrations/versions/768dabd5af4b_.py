"""empty message

Revision ID: 768dabd5af4b
Revises: b13aab61bc58
Create Date: 2024-04-24 19:50:19.731214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '768dabd5af4b'
down_revision: Union[str, None] = 'b13aab61bc58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('code_id', sa.String(), nullable=True))
    op.drop_column('users', 'uuid_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uuid_id', sa.VARCHAR(), nullable=True))
    op.drop_column('users', 'code_id')
    # ### end Alembic commands ###
