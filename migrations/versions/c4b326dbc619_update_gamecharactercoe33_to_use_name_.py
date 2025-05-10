"""
Migration to update GameCharacterCOE33 to use name as primary key.
"""

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'c4b326dbc619'
down_revision = '7bcd9f06141e'
branch_labels = None
depends_on = None

def upgrade():
    # Example migration logic (replace with actual changes)
    pass

def downgrade():
    # Example rollback logic (replace with actual changes)
    pass