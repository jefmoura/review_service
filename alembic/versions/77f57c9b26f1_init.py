"""init

Revision ID: 77f57c9b26f1
Revises: 
Create Date: 2021-01-11 17:41:12.197784

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '77f57c9b26f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('rate', sa.Float(), nullable=False),
    sa.Column('reference_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creator_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_id'), 'review', ['id'], unique=True)
    op.create_table('review_answer',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('review_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creator_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_answer_id'), 'review_answer', ['id'], unique=True)
    op.create_table('review_event',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('type', postgresql.ENUM('LIKE', 'REPORT', name='review_eventtype'), nullable=False),
    sa.Column('review_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('creator_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_event_id'), 'review_event', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_review_event_id'), table_name='review_event')
    op.drop_table('review_event')
    op.drop_index(op.f('ix_review_answer_id'), table_name='review_answer')
    op.drop_table('review_answer')
    op.drop_index(op.f('ix_review_id'), table_name='review')
    op.drop_table('review')
    # ### end Alembic commands ###
