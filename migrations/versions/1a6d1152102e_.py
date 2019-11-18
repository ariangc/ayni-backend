"""empty message

Revision ID: 1a6d1152102e
Revises: ae8f349a0dad
Create Date: 2019-09-15 19:09:33.515474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a6d1152102e'
down_revision = 'ae8f349a0dad'
branch_labels = None
depends_on = None


def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.create_table('like',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('name', sa.String(length=100), nullable=True),
	sa.Column('description', sa.String(length=1000), nullable=True),
	sa.Column('logodir', sa.String(length=500), nullable=True),
	sa.Column('create_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
	sa.Column('last_mod_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
	sa.PrimaryKeyConstraint('id'),
	sa.UniqueConstraint('logodir'),
	sa.UniqueConstraint('name')
	)
	# ### end Alembic commands ###


def downgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table('like')
	# ### end Alembic commands ###
