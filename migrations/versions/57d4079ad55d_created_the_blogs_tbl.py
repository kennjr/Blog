"""Created the blogs tbl

Revision ID: 57d4079ad55d
Revises: 36a8b56240f4
Create Date: 2022-03-14 14:36:13.130799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57d4079ad55d'
down_revision = '36a8b56240f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_txt', sa.String(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.String(length=255), nullable=True),
    sa.Column('saves', sa.String(), nullable=True),
    sa.Column('comments', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs')
    # ### end Alembic commands ###
