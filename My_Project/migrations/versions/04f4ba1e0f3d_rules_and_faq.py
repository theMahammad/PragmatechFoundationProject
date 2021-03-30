"""Rules and Faq

Revision ID: 04f4ba1e0f3d
Revises: 
Create Date: 2021-03-30 14:11:34.309485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04f4ba1e0f3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('content', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_rules'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rules')
    # ### end Alembic commands ###