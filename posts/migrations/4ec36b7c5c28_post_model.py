"""post model

Revision ID: 4ec36b7c5c28
Revises: 818fc3bbc28a
Create Date: 2022-01-19 12:35:55.971329

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '4ec36b7c5c28'
down_revision = '818fc3bbc28a'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.Unicode(length=255), nullable=False))
        batch_op.add_column(sa.Column('body', sa.Unicode(length=255), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('body')
        batch_op.drop_column('title')

    # ### end Alembic commands ###