"""Subscription

Revision ID: 7c0f921f29d7
Revises: 04f4ba1e0f3d
Create Date: 2021-03-30 14:13:29.485133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c0f921f29d7'
down_revision = '04f4ba1e0f3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mail', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_subscription'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscription')
    # ### end Alembic commands ###