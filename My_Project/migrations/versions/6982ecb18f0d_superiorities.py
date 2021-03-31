"""Superiorities

Revision ID: 6982ecb18f0d
Revises: b2034dc7c0b5
Create Date: 2021-03-31 15:20:45.767943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6982ecb18f0d'
down_revision = 'b2034dc7c0b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('superiorities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_superiorities'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('superiorities')
    # ### end Alembic commands ###
