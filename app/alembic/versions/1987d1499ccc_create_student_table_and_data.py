"""create_student_table_and_data

Revision ID: 1987d1499ccc
Revises: 
Create Date: 2023-05-23 12:36:08.919767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1987d1499ccc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the table
    op.create_table(
        'student',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('document', sa.Integer(), nullable=False),
        sa.Column('address', sa.String(length=50), nullable=False),
        sa.Column('subject_id', sa.Integer(), sa.ForeignKey('subject.id'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('document')
    )

    # Insert data into the table
    op.bulk_insert(
        'student',
        [
            {'name': 'John Doe', 'document': 123456789, 'address': '123 Main St', 'subject_id': None},
            {'name': 'Jane Smith', 'document': 987654321, 'address': '456 Elm St', 'subject_id': None}
            # Add more data as needed
        ]
    )


def downgrade():
    op.drop_table('student')