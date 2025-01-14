"""empty message

Revision ID: 5857683fef96
Revises: 
Create Date: 2023-04-28 11:08:47.978712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5857683fef96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('personality', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cat')
    # ### end Alembic commands ###
