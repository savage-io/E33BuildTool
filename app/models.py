from . import db
from sqlalchemy.sql import func

# --- Association Tables for Many-to-Many Relationships ---
build_skills_association = db.Table(
    'build_skills_association_coe33',
    db.Column('user_build_id', db.Integer, db.ForeignKey('user_builds_coe33.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skills_coe33.id'), primary_key=True)
)

build_pictos_association = db.Table(
    'build_pictos_association_coe33',
    db.Column('user_build_id', db.Integer, db.ForeignKey('user_builds_coe33.id'), primary_key=True),
    db.Column('picto_id', db.Integer, db.ForeignKey('pictos_coe33.id'), primary_key=True)
)

build_luminas_association = db.Table(
    'build_luminas_association_coe33',
    db.Column('user_build_id', db.Integer, db.ForeignKey('user_builds_coe33.id'), primary_key=True),
    db.Column('lumina_id', db.Integer, db.ForeignKey('luminas_coe33.id'), primary_key=True)
)

# --- Core Models ---
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(100), unique=True, nullable=False, index=True)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    profile_info = db.Column(db.Text, nullable=True)
    avatar_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", back_populates="owner")
    comments = db.relationship("Comment", back_populates="user")


class GameCharacterCOE33(db.Model):
    __tablename__ = 'game_characters_coe33'  # Corrected table name
    name = db.Column(db.String(100), primary_key=True, unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    base_stats_json = db.Column(db.JSON, nullable=True)
    unique_mechanic_description = db.Column(db.Text, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", back_populates="character")


class SkillCOE33(db.Model):
    __tablename__ = 'skills_coe33'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    ap_cost = db.Column(db.Integer, nullable=True)
    effects_json = db.Column(db.JSON, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)
    character_name = db.Column(db.String(100), nullable=True, index=True)
    mechanics_json = db.Column(db.JSON, nullable=True)
    is_gradient_attack = db.Column(db.Boolean, default=False, nullable=False)

    builds = db.relationship("UserBuildCOE33", secondary=build_skills_association, back_populates="selected_skills")


class PictoCOE33(db.Model):
    __tablename__ = 'pictos_coe33'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150), unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    stat_bonuses_json = db.Column(db.JSON, nullable=True)
    associated_lumina_id = db.Column(db.Integer, db.ForeignKey('luminas_coe33.id'), nullable=True, unique=True)
    how_to_acquire = db.Column(db.Text, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    lumina = db.relationship("LuminaCOE33", backref="source_picto")
    builds = db.relationship("UserBuildCOE33", secondary=build_pictos_association, back_populates="equipped_pictos")


class LuminaCOE33(db.Model):
    __tablename__ = 'luminas_coe33'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150), unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    lumina_point_cost = db.Column(db.Integer, nullable=False, default=1)
    effect_details_json = db.Column(db.JSON, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", secondary=build_luminas_association, back_populates="assigned_luminas")


class UserBuildCOE33(db.Model):
    __tablename__ = 'user_builds_coe33'
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    character_id = db.Column(db.String(100), db.ForeignKey('game_characters_coe33.name'), nullable=False)
    build_title = db.Column(db.String(200), nullable=False)
    build_description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    is_public = db.Column(db.Boolean, default=True)
    rating_score = db.Column(db.Float, default=0.0)
    total_views = db.Column(db.Integer, default=0)

    owner = db.relationship("User", back_populates="builds")
    character = db.relationship("GameCharacterCOE33", back_populates="builds")

    selected_skills = db.relationship("SkillCOE33", secondary=build_skills_association, back_populates="builds")
    equipped_pictos = db.relationship("PictoCOE33", secondary=build_pictos_association, back_populates="builds")
    assigned_luminas = db.relationship("LuminaCOE33", secondary=build_luminas_association, back_populates="builds")


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    build_id = db.Column(db.Integer, db.ForeignKey('user_builds_coe33.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user = db.relationship("User", back_populates="comments")
    build = db.relationship("UserBuildCOE33", backref="comments")


class Item(db.Model):
    __tablename__ = 'items' # This should be one of the first lines after class declaration
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150), unique=True, nullable=False, index=True)
    item_type = db.Column(db.String(50), nullable=False)
    element = db.Column(db.String(50), nullable=True)

    # Power at each level from 1 to 33
    power_by_level_json = db.Column(db.JSON, nullable=True)

    # Attribute scaling changes at specific levels
    attribute_scaling_tiers_json = db.Column(db.JSON, nullable=True)

    # Passive effects unlocked at different levels
    passive_effects_by_level_json = db.Column(db.JSON, nullable=True)

    # Acquisition and other metadata
    acquisition_info = db.Column(db.Text, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)
    primary_character_name = db.Column(db.String(100), nullable=True, index=True)
    metadata_json = db.Column(db.JSON, nullable=True)
    
    # Add relationships if items are directly part of builds (e.g., equipped weapons)
    # If items are directly equipped in builds, you'd need an association table or a ForeignKey in UserBuildCOE33
    # For now, your UserBuildCOE33 uses Pictos, which might encompass equippable items/weapons.
    # If 'Item' is specifically for weapons that ARE pictos, the structure is fine.
    # If 'Item' is for generic gear AND pictos are separate, you might need another relationship for UserBuildCOE33 <-> Item