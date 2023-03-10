"""empty message

Revision ID: bc61b56eaad6
Revises: 
Create Date: 2022-12-12 19:04:14.257284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc61b56eaad6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kargo',
    sa.Column('kargo_id', sa.BigInteger(), nullable=False),
    sa.Column('kargo_alici', sa.String(length=255), nullable=True),
    sa.Column('kargo_gonderici', sa.String(length=255), nullable=True),
    sa.Column('kargo_en', sa.Float(), nullable=True),
    sa.Column('kargo_boy', sa.Float(), nullable=True),
    sa.Column('kargo_yukseklik', sa.Float(), nullable=True),
    sa.Column('kargo_agirlik', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('kargo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kargo')
    # ### end Alembic commands ###
