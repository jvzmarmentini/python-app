"""create_subject_and_student

Revision ID: b8bebab9caa3
Revises: 
Create Date: 2023-05-23 13:58:14.546072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8bebab9caa3'
down_revision = None
branch_labels = None
depends_on = None


"""create_subject_and_student

Revision ID: 7187ea8e23dd
Revises: 1987d1499ccc
Create Date: 2023-05-23 13:52:38.653491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7187ea8e23dd'
down_revision = '1987d1499ccc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'subject',
        sa.Column('class_num', sa.Integer, primary_key=True),
        sa.Column('id', sa.Integer, unique=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('schedule', sa.String(10), nullable=False),
    )

    # Populate the subject table
    op.bulk_insert(
        'subject',
        [
            {'class_num': 1, 'id': 1, 'name': 'Math', 'schedule': 'MWF'},
            {'class_num': 2, 'id': 2, 'name': 'Science', 'schedule': 'TTh'},
            # Add more subjects here
        ]
    )

def downgrade():
    op.drop_table('subject')