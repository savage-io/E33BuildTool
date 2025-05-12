"""New migration for existing schema

Revision ID: d04033442f4e
Revises: rebuilt_migration_script
Create Date: 2025-05-11 22:39:40.041100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd04033442f4e'
down_revision = 'rebuilt_migration_script'
branch_labels = None
depends_on = None


def upgrade():
    # Create or update tables based on the current schema
    if not op.get_bind().engine.dialect.has_table(op.get_bind(), 'characters'):
        op.create_table(
            'characters',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(255), nullable=False, unique=True)
        )

    if not op.get_bind().engine.dialect.has_table(op.get_bind(), 'skills'):
        op.create_table(
            'skills',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(255), nullable=False, unique=True)
        )

    if not op.get_bind().engine.dialect.has_table(op.get_bind(), 'user_builds'):
        op.create_table(
            'user_builds',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(255), nullable=False)
        )

    # Add indexes and foreign keys as needed
    op.create_index('ix_characters_name', 'characters', ['name'], unique=True)
    op.create_index('ix_skills_name', 'skills', ['name'], unique=True)
    op.create_index('ix_user_builds_id', 'user_builds', ['id'], unique=False)

def downgrade():
    # Drop tables and indexes in reverse order
    op.drop_index('ix_user_builds_id', table_name='user_builds')
    op.drop_index('ix_skills_name', table_name='skills')
    op.drop_index('ix_characters_name', table_name='characters')

    op.drop_table('user_builds')
    op.drop_table('skills')
    op.drop_table('characters')
