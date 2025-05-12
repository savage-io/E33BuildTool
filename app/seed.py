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
    """Seeds weapon data from MAELLE_WEAPON_DEFINITIONS."""

    all_weapon_definitions_by_char = [
        ("Maelle", MAELLE_WEAPON_DEFINITIONS),
        # Potentially add other characters here later
    ]

    for character_name, definitions_list in all_weapon_definitions_by_char:
        if not definitions_list:
            click.echo(f"No weapon definitions found for {character_name}. Skipping.")
            continue

        click.echo(f"Seeding weapons for {character_name}...")

        for weapon_data in definitions_list:
            weapon_name = weapon_data.get("name")
            if not weapon_name:
                click.echo(f"Warning: Weapon data found without a name. Skipping: {weapon_data}")
                continue

            existing_weapon = Weapon.query.filter_by(name=weapon_name).first()

            weapon_payload = {
                "weapon_type": weapon_data.get("weapon_type", weapon_data.get("item_type", "Unknown")),
                "element": weapon_data.get("element"),
                "power_by_level_json": weapon_data.get("power_by_level"),
                "attribute_scaling_tiers_json": weapon_data.get("attribute_scaling_tiers"),
                "passive_effects_by_level_json": weapon_data.get("passive_effects"),
                "acquisition_info": weapon_data.get("acquisition_info"),
                "icon_url": weapon_data.get("icon_url"),
                "character_restriction_name": weapon_data.get("character_restriction_name", weapon_data.get("primary_character_name", character_name)),
                "spoiler_info_json": weapon_data.get("spoiler_info_json"),
                "metadata_json": {
                    "stance_synergy": weapon_data.get("stance_synergy", []),
                    "element_interactions": weapon_data.get("element_interactions", {}),
                    "max_level": weapon_data.get("max_level"),
                    "power_at_max_level": weapon_data.get("power at max level"),
                    "attributes_list": weapon_data.get("attributes")
                }
            }

            weapon_payload["metadata_json"] = {k: v for k, v in weapon_payload["metadata_json"].items() if v is not None}

            if existing_weapon:
                click.echo(f"Weapon '{weapon_name}' already exists. Updating...")
                for key, value in weapon_payload.items():
                    setattr(existing_weapon, key, value)
            else:
                click.echo(f"Creating weapon '{weapon_name}'...")
                new_weapon = Weapon(name=weapon_name, **weapon_payload)
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

@click.command(name='seed_pictos_luminas')
@with_appcontext
def seed_pictos_luminas_command():
    """Seeds Picto Lumina data into a single table."""

    from .game_data_definitions.picto_lumina import PICTOS_LUMINAS_DEFINITIONS
    from .models import PictoLumina

    click.echo("Seeding Picto Lumina data...")

    for lumina_data in PICTOS_LUMINAS_DEFINITIONS:
        lumina_name = lumina_data.get("name")
        if not lumina_name:
            click.echo("Warning: Lumina data found without a name. Skipping.")
            continue

        existing_lumina = PictoLumina.query.filter_by(name=lumina_name).first()

        if existing_lumina:
            click.echo(f"Lumina '{lumina_name}' already exists. Updating...")
            existing_lumina.description = lumina_data.get("lumina_description")
            existing_lumina.lp_cost = lumina_data.get("lumina_lp_cost")
            existing_lumina.lumina_type = lumina_data.get("lumina_type")
            existing_lumina.effect_details_json = lumina_data.get("lumina_effect_details_json")
            existing_lumina.picto_variants_json = lumina_data.get("picto_variants_json")
            existing_lumina.tags_json = lumina_data.get("tags_json")
            existing_lumina.spoiler_info_json = lumina_data.get("spoiler_info_json")
        else:
            click.echo(f"Creating Lumina '{lumina_name}'...")
            new_lumina = PictoLumina(
                name=lumina_name,
                description=lumina_data.get("lumina_description"),
                lp_cost=lumina_data.get("lumina_lp_cost"),
                type=lumina_data.get("lumina_type"),
                effect_details_json=lumina_data.get("lumina_effect_details_json"),
                picto_variants_json=lumina_data.get("picto_variants_json"),
                tags_json=lumina_data.get("tags_json"),
                spoiler_info_json=lumina_data.get("spoiler_info_json")
            )
            db.session.add(new_lumina)

    try:
        db.session.commit()
        click.echo("Successfully committed Picto Lumina updates/creations to database.")
    except Exception as e:
        db.session.rollback()
        click.echo(f"Error committing Picto Lumina data to database: {e}")
