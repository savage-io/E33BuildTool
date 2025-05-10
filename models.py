from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON, Table, Boolean, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

# Define the base for declarative models
Base = declarative_base()

# --- Association Tables for Many-to-Many Relationships ---

# For UserBuildCOE33 and SkillCOE33
build_skills_association = Table(
    'build_skills_association_coe33', Base.metadata,
    Column('user_build_id', Integer, ForeignKey('user_builds_coe33.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills_coe33.id'), primary_key=True)
)

# For UserBuildCOE33 and PictoCOE33 (Equipped Pictos)
build_pictos_association = Table(
    'build_pictos_association_coe33', Base.metadata,
    Column('user_build_id', Integer, ForeignKey('user_builds_coe33.id'), primary_key=True),
    Column('picto_id', Integer, ForeignKey('pictos_coe33.id'), primary_key=True),
    Column('picto_slot', Integer, nullable=True)  # Optional: Slot numbers for Pictos (1, 2, or 3)
)

# For UserBuildCOE33 and LuminaCOE33 (Assigned Luminas)
build_luminas_association = Table(
    'build_luminas_association_coe33', Base.metadata,
    Column('user_build_id', Integer, ForeignKey('user_builds_coe33.id'), primary_key=True),
    Column('lumina_id', Integer, ForeignKey('luminas_coe33.id'), primary_key=True)
)

# --- Core Models ---

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(150), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    profile_info = Column(Text, nullable=True)  # For bio/links
    avatar_url = Column(String(255), nullable=True)  # Optional: User avatars

    builds = relationship("UserBuildCOE33", back_populates="owner")
    comments = relationship("Comment", back_populates="user")  # User comments on builds


class GameCharacterCOE33(Base):
    __tablename__ = 'game_characters_coe33'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    base_stats_json = Column(JSON, nullable=True)  # Flexible storage for stats
    unique_mechanic_description = Column(Text, nullable=True)
    icon_url = Column(String(255), nullable=True)

    builds = relationship("UserBuildCOE33", back_populates="character")


class SkillCOE33(Base):
    __tablename__ = 'skills_coe33'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, index=True)
    description = Column(Text, nullable=False)
    ap_cost = Column(Integer, nullable=True)
    effects_json = Column(JSON, nullable=True)  # Complex skill effects
    icon_url = Column(String(255), nullable=True)

    builds = relationship("UserBuildCOE33", secondary=build_skills_association, back_populates="selected_skills")


class PictoCOE33(Base):
    __tablename__ = 'pictos_coe33'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    stat_bonuses_json = Column(JSON, nullable=True)  # Stat bonuses
    associated_lumina_id = Column(Integer, ForeignKey('luminas_coe33.id'), nullable=True, unique=True)
    how_to_acquire = Column(Text, nullable=True)
    icon_url = Column(String(255), nullable=True)

    lumina = relationship("LuminaCOE33", backref="source_picto")


class LuminaCOE33(Base):
    __tablename__ = 'luminas_coe33'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=False)
    lumina_point_cost = Column(Integer, nullable=False, default=1)
    effect_details_json = Column(JSON, nullable=True)  # Complex passive logic
    icon_url = Column(String(255), nullable=True)

    builds = relationship("UserBuildCOE33", secondary=build_luminas_association, back_populates="assigned_luminas")


class UserBuildCOE33(Base):
    __tablename__ = 'user_builds_coe33'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('game_characters_coe33.id'), nullable=False)
    build_title = Column(String(200), nullable=False)
    build_description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())
    is_public = Column(Boolean, default=True)
    rating_score = Column(Float, default=0.0)
    total_views = Column(Integer, default=0)

    owner = relationship("User", back_populates="builds")
    character = relationship("GameCharacterCOE33", back_populates="builds")

    selected_skills = relationship("SkillCOE33", secondary=build_skills_association, back_populates="builds")
    equipped_pictos = relationship("PictoCOE33", secondary=build_pictos_association, back_populates="builds")
    assigned_luminas = relationship("LuminaCOE33", secondary=build_luminas_association, back_populates="builds")


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('user_builds_coe33.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="comments")
    build = relationship("UserBuildCOE33", backref="comments")