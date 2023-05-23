"""enrollment

Revision ID: 315c3a7a18d0
Revises: 7187ea8e23dd
Create Date: 2023-05-23 15:44:19.798477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '315c3a7a18d0'
down_revision = '7187ea8e23dd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the table
    op.create_table(
        'enrollment',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('subject_id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    pass
