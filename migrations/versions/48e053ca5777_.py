"""empty message

Revision ID: 48e053ca5777
Revises: 19bcfb875602
Create Date: 2019-11-02 23:15:02.111733

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '48e053ca5777'
down_revision = '19bcfb875602'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organization', sa.Column('id_creator', sa.Integer(), nullable=True))
    op.drop_column('organization', 'idCreator')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organization', sa.Column('idCreator', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('organization', 'id_creator')
    # ### end Alembic commands ###
