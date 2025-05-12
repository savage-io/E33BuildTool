"""Rebuilt migration script to rename tables and update schema

Revision ID: rebuilt_migration_script
Revises: 4b1642427748
Create Date: 2025-05-11

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# revision identifiers, used by Alembic.
revision = 'rebuilt_migration_script'
down_revision = '4b1642427748'
branch_labels = None
depends_on = None

def table_exists(table_name):
    engine = op.get_bind().engine
    inspector = Inspector.from_engine(engine)
    return table_name in inspector.get_table_names()

def index_exists(table_name, index_name):
    engine = op.get_bind().engine
    inspector = Inspector.from_engine(engine)
    if table_name in inspector.get_table_names():
        return index_name in [index['name'] for index in inspector.get_indexes(table_name)]
    return False

def upgrade():
    # Rename tables if they exist
    if table_exists('game_characters_coe33'):
        logging.info("Renaming table 'game_characters_coe33' to 'characters'")
        op.rename_table('game_characters_coe33', 'characters')
    else:
        logging.info("Table 'game_characters_coe33' does not exist")

    if table_exists('skills_coe33'):
        logging.info("Renaming table 'skills_coe33' to 'skills'")
        op.rename_table('skills_coe33', 'skills')
    else:
        logging.info("Table 'skills_coe33' does not exist")

    if table_exists('user_builds_coe33'):
        logging.info("Renaming table 'user_builds_coe33' to 'user_builds'")
        op.rename_table('user_builds_coe33', 'user_builds')
    else:
        logging.info("Table 'user_builds_coe33' does not exist")

    # Update indexes and foreign keys
    if table_exists('characters'):
        logging.info("Updating indexes for table 'characters'")
        with op.batch_alter_table('characters', schema=None) as batch_op:
            if index_exists('characters', 'ix_game_characters_coe33_name'):
                logging.info("Dropping index 'ix_game_characters_coe33_name'")
                batch_op.drop_index('ix_game_characters_coe33_name')
            else:
                logging.info("Index 'ix_game_characters_coe33_name' does not exist")
            logging.info("Creating index 'ix_characters_name'")
            batch_op.create_index('ix_characters_name', ['name'], unique=True)

    if table_exists('skills'):
        logging.info("Updating indexes for table 'skills'")
        with op.batch_alter_table('skills', schema=None) as batch_op:
            if index_exists('skills', 'ix_skills_coe33_name'):
                logging.info("Dropping index 'ix_skills_coe33_name'")
                batch_op.drop_index('ix_skills_coe33_name')
            else:
                logging.info("Index 'ix_skills_coe33_name' does not exist")
            logging.info("Creating index 'ix_skills_name'")
            batch_op.create_index('ix_skills_name', ['name'], unique=True)

    if table_exists('user_builds'):
        logging.info("Updating indexes for table 'user_builds'")
        with op.batch_alter_table('user_builds', schema=None) as batch_op:
            if index_exists('user_builds', 'ix_user_builds_coe33_id'):
                logging.info("Dropping index 'ix_user_builds_coe33_id'")
                batch_op.drop_index('ix_user_builds_coe33_id')
            else:
                logging.info("Index 'ix_user_builds_coe33_id' does not exist")
            logging.info("Creating index 'ix_user_builds_id'")
            batch_op.create_index('ix_user_builds_id', ['id'], unique=False)

    # Update foreign keys in related tables
    if table_exists('build_assigned_pictoluminas'):
        logging.info("Updating foreign keys for table 'build_assigned_pictoluminas'")
        with op.batch_alter_table('build_assigned_pictoluminas', schema=None) as batch_op:
            logging.info("Dropping existing foreign key constraint")
            batch_op.drop_constraint(None, type_='foreignkey')
            logging.info("Creating new foreign key constraint")
            batch_op.create_foreign_key(None, 'user_builds', ['user_build_id'], ['id'], ondelete='CASCADE')

    if table_exists('build_equipped_pictos'):
        logging.info("Updating foreign keys for table 'build_equipped_pictos'")
        with op.batch_alter_table('build_equipped_pictos', schema=None) as batch_op:
            logging.info("Dropping existing foreign key constraint")
            batch_op.drop_constraint(None, type_='foreignkey')
            logging.info("Creating new foreign key constraint")
            batch_op.create_foreign_key(None, 'user_builds', ['user_build_id'], ['id'], ondelete='CASCADE')

    if table_exists('build_skills_association'):
        logging.info("Updating foreign keys for table 'build_skills_association'")
        with op.batch_alter_table('build_skills_association', schema=None) as batch_op:
            logging.info("Dropping existing foreign key constraint")
            batch_op.drop_constraint(None, type_='foreignkey')
            logging.info("Creating new foreign key constraint")
            batch_op.create_foreign_key(None, 'skills', ['skill_id'], ['id'], ondelete='CASCADE')

    if table_exists('comments'):
        logging.info("Updating foreign keys for table 'comments'")
        with op.batch_alter_table('comments', schema=None) as batch_op:
            logging.info("Dropping existing foreign key constraint")
            batch_op.drop_constraint(None, type_='foreignkey')
            logging.info("Creating new foreign key constraint")
            batch_op.create_foreign_key(None, 'user_builds', ['build_id'], ['id'], ondelete='CASCADE')

    # Update the upgrade function to check for table existence before altering
    if table_exists('weapons') and table_exists('game_characters_coe33'):
        logging.info("Updating foreign keys for table 'weapons'")
        with op.batch_alter_table('weapons', schema=None) as batch_op:
            logging.info("Dropping existing foreign key constraint")
            batch_op.drop_constraint(None, type_='foreignkey')
            logging.info("Creating new foreign key constraint")
            batch_op.create_foreign_key(None, 'characters', ['character_restriction_name'], ['name'])

def downgrade():
    # Reverse the renaming of tables
    if table_exists('characters'):
        op.rename_table('characters', 'game_characters_coe33')
    if table_exists('skills'):
        op.rename_table('skills', 'skills_coe33')
    if table_exists('user_builds'):
        op.rename_table('user_builds', 'user_builds_coe33')

    # Reverse indexes and foreign keys
    if table_exists('game_characters_coe33'):
        with op.batch_alter_table('game_characters_coe33', schema=None) as batch_op:
            if index_exists('game_characters_coe33', 'ix_characters_name'):
                batch_op.drop_index('ix_characters_name')
            batch_op.create_index('ix_game_characters_coe33_name', ['name'], unique=True)

    if table_exists('skills_coe33'):
        with op.batch_alter_table('skills_coe33', schema=None) as batch_op:
            if index_exists('skills_coe33', 'ix_skills_name'):
                batch_op.drop_index('ix_skills_name')
            batch_op.create_index('ix_skills_coe33_name', ['name'], unique=True)

    if table_exists('user_builds_coe33'):
        with op.batch_alter_table('user_builds_coe33', schema=None) as batch_op:
            if index_exists('user_builds_coe33', 'ix_user_builds_id'):
                batch_op.drop_index('ix_user_builds_id')
            batch_op.create_index('ix_user_builds_coe33_id', ['id'], unique=False)

    # Reverse foreign keys in related tables
    if table_exists('build_assigned_pictoluminas'):
        with op.batch_alter_table('build_assigned_pictoluminas', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'user_builds_coe33', ['user_build_id'], ['id'], ondelete='CASCADE')

    if table_exists('build_equipped_pictos'):
        with op.batch_alter_table('build_equipped_pictos', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'user_builds_coe33', ['user_build_id'], ['id'], ondelete='CASCADE')

    if table_exists('build_skills_association'):
        with op.batch_alter_table('build_skills_association', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'skills_coe33', ['skill_id'], ['id'], ondelete='CASCADE')

    if table_exists('comments'):
        with op.batch_alter_table('comments', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'user_builds_coe33', ['build_id'], ['id'], ondelete='CASCADE')
