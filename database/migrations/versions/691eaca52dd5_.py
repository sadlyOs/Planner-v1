"""empty message

Revision ID: 691eaca52dd5
Revises: f9f5359d3c26
Create Date: 2024-04-24 20:00:42.469955

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '691eaca52dd5'
down_revision: Union[str, None] = 'f9f5359d3c26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('simplecode', sa.String(), nullable=True))
    op.drop_column('users', 'code_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('code_id', sa.VARCHAR(), nullable=True))
    op.drop_column('users', 'simplecode')
    # ### end Alembic commands ###