"""empty message

Revision ID: b36dcd907e1d
Revises: 9b32067f601a
Create Date: 2019-09-15 21:33:01.927773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36dcd907e1d'
down_revision = '9b32067f601a'
branch_labels = None
depends_on = None


def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.create_table('like_X__user',
	sa.Column('id_user', sa.Integer(), nullable=False),
	sa.Column('id_like', sa.Integer(), nullable=False),
	sa.Column('flg_active', sa.Integer(), nullable=False),
	sa.Column('last_mod_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
	sa.ForeignKeyConstraint(['id_like'], ['like.id'], ),
	sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
	sa.PrimaryKeyConstraint('id_user', 'id_like')
	)
	# ### end Alembic commands ###


def downgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table('like_X__user')
	# ### end Alembic commands ###
