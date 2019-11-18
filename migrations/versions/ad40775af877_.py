"""empty message

Revision ID: ad40775af877
Revises: ec2aa1073ebf
Create Date: 2019-10-21 02:00:02.296335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad40775af877'
down_revision = 'ec2aa1073ebf'
branch_labels = None
depends_on = None


def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.create_table('chat',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('creation_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.Column('last_message_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.PrimaryKeyConstraint('id')
	)
	op.create_table('kanban',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('name', sa.String(length=100), nullable=False),
	sa.Column('description', sa.String(length=255), nullable=False),
	sa.PrimaryKeyConstraint('id')
	)
	op.create_table('notification_type',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('type', sa.String(length=100), nullable=False),
	sa.Column('description', sa.String(length=255), nullable=False),
	sa.Column('content', sa.String(length=255), nullable=False),
	sa.PrimaryKeyConstraint('id')
	)
	op.create_table('message',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('chat_id', sa.Integer(), nullable=False),
	sa.Column('send_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.Column('content', sa.String(length=255), nullable=False),
	sa.Column('flg_visible_sender', sa.Integer(), nullable=False),
	sa.Column('flg_visible_receiver', sa.Integer(), nullable=False),
	sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('id', 'user_id', 'chat_id')
	)
	op.create_table('notification',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('notification_type_id', sa.Integer(), nullable=False),
	sa.Column('description', sa.String(length=255), nullable=False),
	sa.Column('flg_seen', sa.Integer(), nullable=False),
	sa.Column('notification_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.Column('seen_date', sa.DateTime(), nullable=True),
	sa.ForeignKeyConstraint(['notification_type_id'], ['notification_type.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('id')
	)
	op.create_table('points',
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('send_user_id', sa.Integer(), nullable=False),
	sa.Column('quantity', sa.Integer(), nullable=False),
	sa.Column('content', sa.String(length=255), nullable=False),
	sa.Column('send_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.ForeignKeyConstraint(['send_user_id'], ['user.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('user_id', 'send_user_id')
	)
	op.create_table('report',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('send_user_id', sa.Integer(), nullable=False),
	sa.Column('message', sa.String(length=255), nullable=False),
	sa.Column('send_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.ForeignKeyConstraint(['send_user_id'], ['user.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('id', 'user_id', 'send_user_id')
	)
	op.create_table('contact',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('activity_id', sa.Integer(), nullable=False),
	sa.Column('name', sa.String(length=100), nullable=False),
	sa.Column('telephone_number_1', sa.String(length=20), nullable=True),
	sa.Column('telephone_number_2', sa.String(length=20), nullable=True),
	sa.Column('email_1', sa.String(length=50), nullable=True),
	sa.Column('email_2', sa.String(length=50), nullable=True),
	sa.Column('direction', sa.String(length=100), nullable=True),
	sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
	sa.PrimaryKeyConstraint('id')
	)
	op.create_table('kanban_x_activity',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('activity_id', sa.Integer(), nullable=False),
	sa.Column('kanban_type_id', sa.Integer(), nullable=False),
	sa.Column('creation_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.Column('name', sa.String(length=100), nullable=False),
	sa.Column('description', sa.String(length=255), nullable=True),
	sa.Column('modification_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.Column('limit_date', sa.DateTime(), nullable=True),
	sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
	sa.ForeignKeyConstraint(['kanban_type_id'], ['kanban.id'], ),
	sa.PrimaryKeyConstraint('id')
	)
	op.create_table('staff_x_activity',
	sa.Column('activity_id', sa.Integer(), nullable=False),
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('flg_active', sa.Integer(), nullable=False),
	sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('activity_id', 'user_id')
	)
	op.create_table('coments',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('news_id', sa.Integer(), nullable=False),
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('publication_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.Column('type', sa.Integer(), nullable=False),
	sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('id', 'news_id', 'user_id')
	)
	op.create_table('comments',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('news_id', sa.Integer(), nullable=False),
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('publication_date', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
	sa.Column('description', sa.String(length=255), nullable=False),
	sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('id', 'news_id', 'user_id')
	)
	# ### end Alembic commands ###


def downgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table('comments')
	op.drop_table('coments')
	op.drop_table('staff_x_activity')
	op.drop_table('kanban_x_activity')
	op.drop_table('contact')
	op.drop_table('report')
	op.drop_table('points')
	op.drop_table('notification')
	op.drop_table('message')
	op.drop_table('notification_type')
	op.drop_table('kanban')
	op.drop_table('chat')
	# ### end Alembic commands ###
