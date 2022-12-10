"""empty message

Revision ID: 5ea982a70bdb
Revises: 835d318adb1b
Create Date: 2022-12-09 15:02:05.359595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ea982a70bdb'
down_revision = '835d318adb1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin', sa.String(length=3), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('admin')

    # ### end Alembic commands ###