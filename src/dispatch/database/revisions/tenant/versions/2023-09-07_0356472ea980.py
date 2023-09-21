"""Adds new restrict to stable incident priority id

Revision ID: 0356472ea980
Revises: 4e57f5b1f3f3
Create Date: 2023-09-01 15:30:52.512886

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0356472ea980"
down_revision = "4e57f5b1f3f3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("project", sa.Column("stable_priority_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "project", "incident_priority", ["stable_priority_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "project", type_="foreignkey")
    op.drop_column("project", "stable_priority_id")
    # ### end Alembic commands ###