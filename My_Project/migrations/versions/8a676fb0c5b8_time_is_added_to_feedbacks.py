"""time is added to Feedbacks 

Revision ID: 8a676fb0c5b8
Revises: 7e91d4ba99b7
Create Date: 2021-04-07 13:10:06.568910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a676fb0c5b8'
down_revision = '7e91d4ba99b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedback', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=250),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedback', schema=None) as batch_op:
        batch_op.alter_column('time',
               existing_type=sa.String(length=250),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
