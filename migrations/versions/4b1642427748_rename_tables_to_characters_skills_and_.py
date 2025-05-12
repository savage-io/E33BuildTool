"""Rename tables to characters, skills, and user_builds

Revision ID: 4b1642427748
Revises: ac029eb0fa7e
Create Date: 2025-05-11 22:05:55.137462

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import create_engine

# revision identifiers, used by Alembic.
revision = '4b1642427748'
down_revision = 'ac029eb0fa7e'
branch_labels = None
depends_on = None

def table_exists(table_name):
    engine = create_engine(op.get_bind().engine.url)
    inspector = Inspector.from_engine(engine)
    return table_name in inspector.get_table_names()

def index_exists(table_name, index_name):
    engine = create_engine(op.get_bind().engine.url)
    inspector = Inspector.from_engine(engine)
    if table_name in inspector.get_table_names():
        return index_name in [index['name'] for index in inspector.get_indexes(table_name)]
    return False

def upgrade():
    # Check if tables already exist before creating them
    if not table_exists('characters'):
        op.create_table('characters',
            sa.Column('name', sa.String(length=100), nullable=False),
            sa.Column('description', sa.Text(), nullable=True),
            sa.Column('base_stats_json', sa.JSON(), nullable=True),
            sa.Column('unique_mechanic_description', sa.Text(), nullable=True),
            sa.Column('icon_url', sa.String(length=255), nullable=True),
            sa.PrimaryKeyConstraint('name')
        )
        with op.batch_alter_table('characters', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_characters_name'), ['name'], unique=True)

    if not table_exists('skills'):
        op.create_table('skills',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(length=150), nullable=False),
            sa.Column('character_name', sa.String(length=100), nullable=True),
            sa.Column('ap_cost', sa.Integer(), nullable=True),
            sa.Column('description', sa.Text(), nullable=False),
            sa.Column('effects_json', sa.JSON(), nullable=True),
            sa.Column('mechanics_json', sa.JSON(), nullable=True),
            sa.Column('tags_json', sa.JSON(), nullable=True),
            sa.Column('is_gradient_attack', sa.Boolean(), nullable=False),
            sa.Column('spoiler_info_json', sa.JSON(), nullable=True),
            sa.Column('icon_url', sa.String(length=255), nullable=True),
            sa.ForeignKeyConstraint(['character_name'], ['characters.name'], ),
            sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('skills', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_skills_character_name'), ['character_name'], unique=False)
            batch_op.create_index(batch_op.f('ix_skills_id'), ['id'], unique=False)
            batch_op.create_index(batch_op.f('ix_skills_name'), ['name'], unique=True)

    if not table_exists('user_builds'):
        op.create_table('user_builds',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=False),
            sa.Column('character_name', sa.String(length=100), nullable=False),
            sa.Column('build_title', sa.String(length=200), nullable=False),
            sa.Column('build_description', sa.Text(), nullable=True),
            sa.Column('equipped_weapon_id', sa.Integer(), nullable=True),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
            sa.Column('last_updated', sa.DateTime(timezone=True), nullable=True),
            sa.Column('is_public', sa.Boolean(), nullable=True),
            sa.Column('rating_score', sa.Float(), nullable=True),
            sa.Column('total_views', sa.Integer(), nullable=True),
            sa.Column('attribute_points_allocated_json', sa.JSON(), nullable=True),
            sa.Column('character_level_for_build', sa.Integer(), nullable=True),
            sa.Column('weapon_level_for_build', sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(['character_name'], ['characters.name'], ondelete='CASCADE'),
            sa.ForeignKeyConstraint(['equipped_weapon_id'], ['weapons.id'], ),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
            sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('user_builds', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_user_builds_id'), ['id'], unique=False)

    with op.batch_alter_table('game_characters_coe33', schema=None) as batch_op:
        if index_exists('game_characters_coe33', 'ix_game_characters_coe33_name'):
            batch_op.drop_index('ix_game_characters_coe33_name')

    if table_exists('game_characters_coe33'):
        op.drop_table('game_characters_coe33')
        
    with op.batch_alter_table('skills_coe33', schema=None) as batch_op:
        if index_exists('skills_coe33', 'ix_skills_coe33_character_name'):
            batch_op.drop_index('ix_skills_coe33_character_name')
        if index_exists('skills_coe33', 'ix_skills_coe33_id'):
            batch_op.drop_index('ix_skills_coe33_id')
        if index_exists('skills_coe33', 'ix_skills_coe33_name'):
            batch_op.drop_index('ix_skills_coe33_name')

    if table_exists('skills_coe33'):
        op.drop_table('skills_coe33')

    with op.batch_alter_table('user_builds_coe33', schema=None) as batch_op:
        if index_exists('user_builds_coe33', 'ix_user_builds_coe33_id'):
            batch_op.drop_index('ix_user_builds_coe33_id')

    if table_exists('user_builds_coe33'):
        op.drop_table('user_builds_coe33')
        
    if table_exists('user_builds_coe33'):
        with op.batch_alter_table('build_assigned_pictoluminas', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'user_builds', ['user_build_id'], ['id'], ondelete='CASCADE')

    if table_exists('user_builds_coe33'):
        with op.batch_alter_table('build_equipped_pictos', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'user_builds', ['user_build_id'], ['id'], ondelete='CASCADE')

    if table_exists('skills_coe33'):
        with op.batch_alter_table('build_skills_association', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'user_builds', ['user_build_id'], ['id'], ondelete='CASCADE')
            batch_op.create_foreign_key(None, 'skills', ['skill_id'], ['id'], ondelete='CASCADE')

    if table_exists('user_builds_coe33'):
        with op.batch_alter_table('comments', schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.create_foreign_key(None, 'user_builds', ['build_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('weapons', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'characters', ['character_restriction_name'], ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weapons', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'game_characters_coe33', ['character_restriction_name'], ['name'])

    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user_builds_coe33', ['build_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('build_skills_association', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'skills_coe33', ['skill_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'user_builds_coe33', ['user_build_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('build_equipped_pictos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user_builds_coe33', ['user_build_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('build_assigned_pictoluminas', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user_builds_coe33', ['user_build_id'], ['id'], ondelete='CASCADE')

    op.create_table('user_builds_coe33',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('character_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('build_title', sa.VARCHAR(length=200), nullable=False),
    sa.Column('build_description', sa.TEXT(), nullable=True),
    sa.Column('equipped_weapon_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_updated', sa.DATETIME(), nullable=True),
    sa.Column('is_public', sa.BOOLEAN(), nullable=True),
    sa.Column('rating_score', sa.FLOAT(), nullable=True),
    sa.Column('total_views', sa.INTEGER(), nullable=True),
    sa.Column('attribute_points_allocated_json', sqlite.JSON(), nullable=True),
    sa.Column('character_level_for_build', sa.INTEGER(), nullable=True),
    sa.Column('weapon_level_for_build', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['character_name'], ['game_characters_coe33.name'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['equipped_weapon_id'], ['weapons.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_builds_coe33', schema=None) as batch_op:
        batch_op.create_index('ix_user_builds_coe33_id', ['id'], unique=False)

    op.create_table('skills_coe33',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('character_name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('ap_cost', sa.INTEGER(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('effects_json', sqlite.JSON(), nullable=True),
    sa.Column('mechanics_json', sqlite.JSON(), nullable=True),
    sa.Column('tags_json', sqlite.JSON(), nullable=True),
    sa.Column('is_gradient_attack', sa.BOOLEAN(), nullable=False),
    sa.Column('spoiler_info_json', sqlite.JSON(), nullable=True),
    sa.Column('icon_url', sa.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['character_name'], ['game_characters_coe33.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('skills_coe33', schema=None) as batch_op:
        batch_op.create_index('ix_skills_coe33_name', ['name'], unique=1)
        batch_op.create_index('ix_skills_coe33_id', ['id'], unique=False)
        batch_op.create_index('ix_skills_coe33_character_name', ['character_name'], unique=False)

    op.create_table('game_characters_coe33',
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('base_stats_json', sqlite.JSON(), nullable=True),
    sa.Column('unique_mechanic_description', sa.TEXT(), nullable=True),
    sa.Column('icon_url', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    with op.batch_alter_table('game_characters_coe33', schema=None) as batch_op:
        batch_op.create_index('ix_game_characters_coe33_name', ['name'], unique=1)

    with op.batch_alter_table('user_builds', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_builds_id'))

    op.drop_table('user_builds')
    with op.batch_alter_table('skills', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_skills_name'))
        batch_op.drop_index(batch_op.f('ix_skills_id'))
        batch_op.drop_index(batch_op.f('ix_skills_character_name'))

    op.drop_table('skills')
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_characters_name'))

    op.drop_table('characters')
    # ### end Alembic commands ###
