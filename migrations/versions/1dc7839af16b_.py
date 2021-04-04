"""empty message

Revision ID: 1dc7839af16b
Revises: 
Create Date: 2021-04-02 14:27:21.659316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dc7839af16b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('opening_price', sa.Float(), nullable=True),
    sa.Column('closing_price', sa.Float(), nullable=True),
    sa.Column('min_price', sa.Float(), nullable=True),
    sa.Column('max_price', sa.Float(), nullable=True),
    sa.Column('average_price', sa.Float(), nullable=True),
    sa.Column('units_traded', sa.Float(), nullable=True),
    sa.Column('volume_1day', sa.Float(), nullable=True),
    sa.Column('volume_7day', sa.Float(), nullable=True),
    sa.Column('buy_price', sa.Float(), nullable=True),
    sa.Column('sell_price', sa.Float(), nullable=True),
    sa.Column('fluctate_24H', sa.Float(), nullable=True),
    sa.Column('fluctate_24H_rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coin')
    # ### end Alembic commands ###
