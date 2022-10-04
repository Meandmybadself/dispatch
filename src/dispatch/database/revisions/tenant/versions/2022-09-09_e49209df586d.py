"""Removes relationship to source in the case data model

Revision ID: e49209df586d
Revises: 4452426c6905
Create Date: 2022-09-09 12:15:44.946539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e49209df586d"
down_revision = "4452426c6905"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("case_source_id_fkey", "case", type_="foreignkey")
    op.drop_column("case", "source_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("case", sa.Column("source_id", sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key("case_source_id_fkey", "case", "source", ["source_id"], ["id"])
    # ### end Alembic commands ###