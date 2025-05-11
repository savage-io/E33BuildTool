import click
from flask.cli import with_appcontext
from . import db
from .models import GameCharacterCOE33
from .game_data_definitions.characters import MAELLE_CHARACTER_DATA
from .models import Weapon
from .game_data_definitions.maelle_weapons import MAELLE_WEAPON_DEFINITIONS
from .game_data_definitions.maelle_skills import MAELLE_SKILL_DEFINITIONS
from .models import SkillCOE33

@click.command(name='seed_maelle_character')
@with_appcontext
def seed_maelle_character_command():
    """Seeds Maelle's core character data."""

    click.echo("Attempting to seed Maelle's character data...")

    # Check if Maelle already exists
    existing_maelle = GameCharacterCOE33.query.filter_by(name=MAELLE_CHARACTER_DATA["name"]).first()
    if (existing_maelle):
        click.echo(f"Character '{MAELLE_CHARACTER_DATA['name']}' already exists. Skipping creation.")
        return

    new_character = GameCharacterCOE33(
        name=MAELLE_CHARACTER_DATA["name"],
        description=MAELLE_CHARACTER_DATA["description"],
        base_stats_json=MAELLE_CHARACTER_DATA["base_stats_json"],
        unique_mechanic_description=MAELLE_CHARACTER_DATA["unique_mechanic_description"],
        icon_url=MAELLE_CHARACTER_DATA["icon_url"]
    )

    db.session.add(new_character)
    try:
        db.session.commit()
        click.echo(f"Successfully created character: {new_character.name}")
        click.echo(f"  Description: {new_character.description[:100]}...")
        click.echo(f"  Base Stats: {new_character.base_stats_json}")
        click.echo(f"  Unique Mechanic: {new_character.unique_mechanic_description[:100]}...")
    except Exception as e:
        db.session.rollback()
        click.echo(f"Error creating Maelle character: {e}")

@click.command(name='seed_weapons')
@with_appcontext
def seed_weapons_command():
    """Seeds weapon data from multiple definitions."""

    all_weapon_definitions_by_char = [
        ("Maelle", MAELLE_WEAPON_DEFINITIONS),
        # Add tuples for other characters, e.g., ("Gustave", GUSTAVE_WEAPON_DEFINITIONS)
    ]

    for character_name, definitions_list in all_weapon_definitions_by_char:
        if not definitions_list:
            click.echo(f"No weapon definitions found for {character_name}. Skipping.")
            continue

        click.echo(f"Seeding weapons for {character_name}...")

        for weapon_data in definitions_list:
            if not isinstance(weapon_data, dict):
                click.echo(f"Warning: Found non-dictionary item in {character_name}'s weapon list. Skipping: {weapon_data}")
                continue

            weapon_name = weapon_data.get("name")
            if not weapon_name:
                click.echo(f"Warning: Weapon data found without a name for {character_name}. Skipping: {weapon_data}")
                continue

            existing_weapon = Weapon.query.filter_by(name=weapon_name).first()

            metadata = {
                "stance_synergy": weapon_data.get("stance_synergy", []),
                "element_interactions": weapon_data.get("element_interactions", {}),
                "max_level": weapon_data.get("max_level"),
                "power_at_max_level": weapon_data.get("power at max level"),
                "attributes_list": weapon_data.get("attributes"),
                "passives_data": weapon_data.get("passive_effects")
            }

            if existing_weapon:
                click.echo(f"Weapon '{weapon_name}' already exists. Updating...")
                existing_weapon.weapons_type = weapon_data.get("weapons_type", "Unknown")
                existing_weapon.element = weapon_data.get("element")
                existing_weapon.power_by_level_json = weapon_data.get("power_by_level")
                existing_weapon.attribute_scaling_tiers_json = weapon_data.get("attribute_scaling_tiers")
                existing_weapon.passive_effects_by_level_json = weapon_data.get("passive_effects")
                existing_weapon.acquisition_info = weapon_data.get("acquisition_info")
                existing_weapon.icon_url = weapon_data.get("icon_url")
                existing_weapon.primary_character_name = character_name
                existing_weapon.metadata_json = metadata
                existing_weapon.spoiler_info_json = weapon_data.get("spoiler_info_json")
            else:
                click.echo(f"Creating weapon '{weapon_name}'...")
                new_weapon = Weapon(
                    name=weapon_name,
                    weapons_type=weapon_data.get("weapons_type", "Unknown"),
                    element=weapon_data.get("element"),
                    power_by_level_json=weapon_data.get("power_by_level"),
                    attribute_scaling_tiers_json=weapon_data.get("attribute_scaling_tiers"),
                    passive_effects_by_level_json=weapon_data.get("passive_effects"),
                    acquisition_info=weapon_data.get("acquisition_info"),
                    icon_url=weapon_data.get("icon_url"),
                    primary_character_name=character_name,
                    metadata_json=metadata,
                    spoiler_info_json=weapon_data.get("spoiler_info_json")
                )
                db.session.add(new_weapon)

    try:
        db.session.commit()
        click.echo("Successfully committed weapon updates/creations to database.")
    except Exception as e:
        db.session.rollback()
        click.echo(f"Error committing weapons to database: {e}")

@click.command(name='seed_maelle_skills')
@with_appcontext
def seed_maelle_skills_command():
    """Seeds Maelle's skill data."""

    click.echo("Attempting to seed Maelle's skill data...")

    for skill_data in MAELLE_SKILL_DEFINITIONS:
        skill_name = skill_data.get("name")
        if not skill_name:
            click.echo("Warning: Skill data found without a name. Skipping.")
            continue

        existing_skill = SkillCOE33.query.filter_by(name=skill_name).first()

        if existing_skill:
            click.echo(f"Skill '{skill_name}' already exists. Updating...")
            existing_skill.description = skill_data.get("description")
            existing_skill.ap_cost = skill_data.get("ap_cost")
            existing_skill.effects_json = skill_data.get("effects_json")
            existing_skill.icon_url = skill_data.get("icon_url")
            existing_skill.character_name = skill_data.get("character_name")
            existing_skill.mechanics_json = skill_data.get("mechanics_json")
            existing_skill.tags_json = skill_data.get("tags_json")
            existing_skill.spoiler_info_json = skill_data.get("spoiler_info_json")
        else:
            click.echo(f"Creating skill '{skill_name}'...")
            new_skill = SkillCOE33(
                name=skill_name,
                description=skill_data.get("description"),
                ap_cost=skill_data.get("ap_cost"),
                effects_json=skill_data.get("effects_json"),
                icon_url=skill_data.get("icon_url"),
                character_name=skill_data.get("character_name"),
                mechanics_json=skill_data.get("mechanics_json"),
                tags_json=skill_data.get("tags_json"),
                spoiler_info_json=skill_data.get("spoiler_info_json")
            )
            db.session.add(new_skill)

    try:
        db.session.commit()
        click.echo("Successfully committed skill updates/creations to database.")
    except Exception as e:
        db.session.rollback()
        click.echo(f"Error committing skills to database: {e}")
