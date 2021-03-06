"""Foo email

Revision ID: 110ed8dcbe18
Revises: cd1026b43f5a
Create Date: 2021-03-24 18:47:49.711549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '110ed8dcbe18'
down_revision = 'cd1026b43f5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('foo_email', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foo', schema=None) as batch_op:
        batch_op.drop_column('foo_email')

    # ### end Alembic commands ###
