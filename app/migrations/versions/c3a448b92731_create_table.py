"""create table

Revision ID: c3a448b92731
Revises: 728b9d6f9c9c
Create Date: 2023-09-04 14:22:11.760815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3a448b92731'
down_revision: Union[str, None] = '728b9d6f9c9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('star_rating', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('restaurant_id', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('customer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reviews', 'customers', ['customer_id'], ['id'])
    op.create_foreign_key(None, 'reviews', 'restaurants', ['restaurant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'customer_id')
    op.drop_column('reviews', 'restaurant_id')
    op.drop_column('reviews', 'star_rating')
    # ### end Alembic commands ###