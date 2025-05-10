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
    db.Column('picto_id', db.Integer, db.ForeignKey('pictos_coe33.id'), primary_key=True),
    db.Column('picto_slot', db.Integer, nullable=True)
)

build_luminas_association = db.Table(
    'build_luminas_association_coe33',
    db.Column('user_build_id', db.Integer, db.ForeignKey('user_builds_coe33.id'), primary_key=True),
    db.Column('lumina_id', db.Integer, db.ForeignKey('luminas_coe33.id'), primary_key=True)
)

# --- Core Models ---
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    profile_info = db.Column(db.Text, nullable=True)
    avatar_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", back_populates="owner")
    comments = db.relationship("Comment", back_populates="user")


class GameCharacterCOE33(db.Model):
    __tablename__ = 'game_characters_coe33'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    base_stats_json = db.Column(db.JSON, nullable=True)
    unique_mechanic_description = db.Column(db.Text, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", back_populates="character")


class SkillCOE33(db.Model):
    __tablename__ = 'skills_coe33'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ap_cost = db.Column(db.Integer, nullable=True)
    effects_json = db.Column(db.JSON, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", secondary=build_skills_association, back_populates="selected_skills")


class PictoCOE33(db.Model):
    __tablename__ = 'pictos_coe33'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    stat_bonuses_json = db.Column(db.JSON, nullable=True)
    associated_lumina_id = db.Column(db.Integer, db.ForeignKey('luminas_coe33.id'), nullable=True, unique=True)
    how_to_acquire = db.Column(db.Text, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    lumina = db.relationship("LuminaCOE33", backref="source_picto")


class LuminaCOE33(db.Model):
    __tablename__ = 'luminas_coe33'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    lumina_point_cost = db.Column(db.Integer, nullable=False, default=1)
    effect_details_json = db.Column(db.JSON, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", secondary=build_luminas_association, back_populates="assigned_luminas")


class UserBuildCOE33(db.Model):
    __tablename__ = 'user_builds_coe33'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('game_characters_coe33.id'), nullable=False)
    build_title = db.Column(db.String(200), nullable=False)
    build_description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
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