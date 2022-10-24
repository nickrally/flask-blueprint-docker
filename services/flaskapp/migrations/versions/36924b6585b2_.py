"""empty message

Revision ID: 36924b6585b2
Revises: 8075d5759e61
Create Date: 2022-10-21 08:19:36.596519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36924b6585b2'
down_revision = '8075d5759e61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thing', sa.Column('description', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('thing', 'description')
    # ### end Alembic commands ###