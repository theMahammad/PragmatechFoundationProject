"""Zoram

Revision ID: 36d27b58fa8c
Revises: 7cc004e6d0cc
Create Date: 2021-04-15 09:03:12.497863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36d27b58fa8c'
down_revision = '7cc004e6d0cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant', schema=None) as batch_op:
        batch_op.drop_constraint('uq_restaurant_slug', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_restaurant_slug', ['slug'])

    # ### end Alembic commands ###
