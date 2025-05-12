from . import db
from sqlalchemy.sql import func
# from sqlalchemy.ext.associationproxy import association_proxy # Not strictly needed for current setup

# --- Association Tables for UserBuildCOE33 ---
build_skills_association = db.Table(
    'build_skills_association', 
    db.Column('user_build_id', db.Integer, db.ForeignKey('user_builds_coe33.id', ondelete='CASCADE'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skills_coe33.id', ondelete='CASCADE'), primary_key=True)
)

build_assigned_luminas_association = db.Table(
    'build_assigned_pictoluminas', 
    db.Column('user_build_id', db.Integer, db.ForeignKey('user_builds_coe33.id', ondelete='CASCADE'), primary_key=True),
    db.Column('pictolumina_id', db.Integer, db.ForeignKey('pictoluminas.id', ondelete='CASCADE'), primary_key=True)
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

    builds = db.relationship("UserBuildCOE33", back_populates="owner", lazy='dynamic', cascade="all, delete-orphan")
    comments = db.relationship("Comment", back_populates="user", lazy='dynamic', cascade="all, delete-orphan")

class GameCharacterCOE33(db.Model):
    __tablename__ = 'game_characters_coe33'
    name = db.Column(db.String(100), primary_key=True, unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    base_stats_json = db.Column(db.JSON, nullable=True) # For base Vit, Might, Agi, Def, Luck, HP, AP etc.
    unique_mechanic_description = db.Column(db.Text, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    builds = db.relationship("UserBuildCOE33", back_populates="character", lazy='dynamic')
    # If you decide to link weapons directly to characters they are exclusive to (one-to-many)
    # weapons = db.relationship("Weapon", back_populates="character_restriction", lazy='dynamic')

class SkillCOE33(db.Model):
    __tablename__ = 'skills_coe33'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150), nullable=False, index=True, unique=True)
    character_name = db.Column(db.String(100), db.ForeignKey('game_characters_coe33.name'), nullable=True, index=True) 
    ap_cost = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=False)
    effects_json = db.Column(db.JSON, nullable=True)
    mechanics_json = db.Column(db.JSON, nullable=True)
    tags_json = db.Column(db.JSON, nullable=True)
    is_gradient_attack = db.Column(db.Boolean, default=False, nullable=False)
    spoiler_info_json = db.Column(db.JSON, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)

    # Optional: If using character_name as FK
    # character_definition = db.relationship("GameCharacterCOE33")


class Weapon(db.Model): # Renamed from Item to Weapon
    __tablename__ = 'weapons' # New table name
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150), unique=True, nullable=False, index=True)
    weapon_type = db.Column(db.String(50), nullable=False) # e.g., "Rapier", "Energy Rifle"
    element = db.Column(db.String(50), nullable=True)
    power_by_level_json = db.Column(db.JSON, nullable=True)
    attribute_scaling_tiers_json = db.Column(db.JSON, nullable=True)
    passive_effects_by_level_json = db.Column(db.JSON, nullable=True)
    acquisition_info = db.Column(db.Text, nullable=True)
    icon_url = db.Column(db.String(255), nullable=True)
    # Changed from primary_character_name to character_restriction_name for clarity, still FKs to GameCharacter
    character_restriction_name = db.Column(db.String(100), db.ForeignKey('game_characters_coe33.name'), nullable=True, index=True)
    metadata_json = db.Column(db.JSON, nullable=True) 
    spoiler_info_json = db.Column(db.JSON, nullable=True)

    # Optional: Relationship back to character if a weapon is exclusive
    # character_restriction = db.relationship("GameCharacterCOE33", back_populates="weapons")
    
    # Relationship to UserBuildCOE33 (if a build has one primary weapon)
    # This would be a one-to-many from Weapon to UserBuildCOE33 if a build has only ONE weapon.
    # Or if a build can have multiple (less common for primary weapon), it would be many-to-many.
    # For now, let's assume a build will have one primary weapon set via a ForeignKey in UserBuildCOE33.


class PictoLumina(db.Model):
    __tablename__ = 'pictoluminas'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150), unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    lp_cost = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=True)
    effect_details_json = db.Column(db.JSON, nullable=True)
    picto_variants_json = db.Column(db.JSON, nullable=True)
    tags_json = db.Column(db.JSON, nullable=True)
    spoiler_info_json = db.Column(db.JSON, nullable=True)
    # general_icon_url = db.Column(db.String(255), nullable=True)

class EquippedPictoInBuild(db.Model):
    __tablename__ = 'build_equipped_pictos'
    user_build_id = db.Column(db.Integer, db.ForeignKey('user_builds_coe33.id', ondelete='CASCADE'), primary_key=True)
    pictolumina_id = db.Column(db.Integer, db.ForeignKey('pictoluminas.id', ondelete='CASCADE'), primary_key=True)
    picto_variant_key = db.Column(db.String(50), primary_key=True)

    build = db.relationship("UserBuildCOE33", back_populates="equipped_picto_associations")
    pictolumina_definition = db.relationship("PictoLumina", backref="equipped_in_builds_as_picto")

    @property
    def stat_bonuses(self):
        if self.pictolumina_definition and self.pictolumina_definition.picto_variants_json:
            variant_data = self.pictolumina_definition.picto_variants_json.get(self.picto_variant_key)
            return variant_data.get("stat_bonuses") if variant_data else None
        return None

    @property
    def picto_display_name(self):
        # (Same as before, provides a nice display name for the specific Picto variant)
        if self.pictolumina_definition and self.pictolumina_definition.picto_variants_json:
            variant_data = self.pictolumina_definition.picto_variants_json.get(self.picto_variant_key)
            if variant_data and variant_data.get("picto_display_name"):
                return variant_data["picto_display_name"]
        return f"{self.pictolumina_definition.name} (Variant {self.picto_variant_key})" if self.pictolumina_definition else "Unknown Picto Variant"


class UserBuildCOE33(db.Model):
    __tablename__ = 'user_builds_coe33'
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    character_name = db.Column(db.String(100), db.ForeignKey('game_characters_coe33.name', ondelete='CASCADE'), nullable=False)
    build_title = db.Column(db.String(200), nullable=False)
    build_description = db.Column(db.Text, nullable=True)
    
    # Foreign Key for the equipped weapon in this build
    equipped_weapon_id = db.Column(db.Integer, db.ForeignKey('weapons.id'), nullable=True) # Assuming a build has one weapon

    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    is_public = db.Column(db.Boolean, default=True)
    rating_score = db.Column(db.Float, default=0.0)
    total_views = db.Column(db.Integer, default=0)
    # User-defined attribute points for this build/character level
    attribute_points_allocated_json = db.Column(db.JSON, nullable=True) # e.g. {"Vitality": 50, "Might": 30 ...}
    character_level_for_build = db.Column(db.Integer, nullable=True) # To calculate max LP, Skill Points etc.
    weapon_level_for_build = db.Column(db.Integer, nullable=True) # Level of the equipped weapon

    owner = db.relationship("User", back_populates="builds")
    character = db.relationship("GameCharacterCOE33", back_populates="builds")
    equipped_weapon = db.relationship("Weapon", backref="used_in_builds") # Relationship to the equipped Weapon

    selected_skills = db.relationship(
        "SkillCOE33", 
        secondary=build_skills_association, 
        backref=db.backref("used_in_builds", lazy='dynamic'), # Changed backref slightly
        lazy='dynamic'
    )
    assigned_luminas = db.relationship(
        "PictoLumina",
        secondary=build_assigned_luminas_association,
        backref=db.backref("used_in_builds_as_lumina", lazy='dynamic'),
        lazy='dynamic'
    )
    equipped_picto_associations = db.relationship("EquippedPictoInBuild", back_populates="build", cascade="all, delete-orphan", lazy='dynamic')

    @property
    def equipped_pictos(self):
        return [{"definition": assoc.pictolumina_definition, "variant_key": assoc.picto_variant_key, "stats": assoc.stat_bonuses, "display_name": assoc.picto_display_name} for assoc in self.equipped_picto_associations]


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    build_id = db.Column(db.Integer, db.ForeignKey('user_builds_coe33.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    user = db.relationship("User", back_populates="comments")
    build = db.relationship("UserBuildCOE33", backref=db.backref("comments", lazy='dynamic', cascade="all, delete-orphan"))