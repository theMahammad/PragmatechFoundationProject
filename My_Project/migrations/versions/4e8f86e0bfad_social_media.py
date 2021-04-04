"""Social Media

Revision ID: 4e8f86e0bfad
Revises: 6982ecb18f0d
Create Date: 2021-04-01 19:53:54.667057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e8f86e0bfad'
down_revision = '6982ecb18f0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('social_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('facebook', sa.String(length=200), nullable=True),
    sa.Column('instagram', sa.String(length=200), nullable=True),
    sa.Column('youtube', sa.String(length=200), nullable=True),
    sa.Column('twitter', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_social_account'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('social_account')
    # ### end Alembic commands ###