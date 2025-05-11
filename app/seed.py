import click
from flask.cli import with_appcontext
from . import db
from .models import GameCharacterCOE33
from .game_data_definitions.characters import MAELLE_CHARACTER_DATA
from .models import Item
from .game_data_definitions.maelle_weapons import MAELLE_WEAPON_DEFINITIONS

@click.command(name='seed_maelle_character')
@with_appcontext
def seed_maelle_character_command():
    """Seeds Maelle's core character data."""

    click.echo("Attempting to seed Maelle's character data...")

    # Check if Maelle already exists
    existing_maelle = GameCharacterCOE33.query.filter_by(name=MAELLE_CHARACTER_DATA["name"]).first()
    if existing_maelle:
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

@click.command(name='seed_maelle_weapons')
@with_appcontext
def seed_maelle_weapons_command():
    """Seeds Maelle's weapon data."""

    click.echo("Seeding Maelle's weapons...")

    for weapon_data in MAELLE_WEAPON_DEFINITIONS:
        existing_weapon = Item.query.filter_by(name=weapon_data["name"]).first()
        if existing_weapon:
            click.echo(f"Weapon '{weapon_data['name']}' already exists. Updating...")
            existing_weapon.item_type = weapon_data.get("item_type", "Unknown")
            existing_weapon.element = weapon_data.get("element")
            existing_weapon.power_by_level_json = weapon_data.get("power_by_level")
            existing_weapon.attribute_scaling_tiers_json = weapon_data.get("attribute_scaling_tiers")
            existing_weapon.passive_effects_by_level_json = weapon_data.get("passive_effects_by_level")
            existing_weapon.acquisition_info = weapon_data.get("acquisition_info")
            existing_weapon.icon_url = weapon_data.get("icon_url")
        else:
            click.echo(f"Creating weapon '{weapon_data['name']}'...")
            new_weapon = Item(
                name=weapon_data["name"],
                item_type=weapon_data.get("item_type", "Unknown"),
                element=weapon_data.get("element"),
                power_by_level_json=weapon_data.get("power_by_level"),
                attribute_scaling_tiers_json=weapon_data.get("attribute_scaling_tiers"),
                passive_effects_by_level_json=weapon_data.get("passive_effects_by_level"),
                acquisition_info=weapon_data.get("acquisition_info"),
                icon_url=weapon_data.get("icon_url")
            )
            db.session.add(new_weapon)

    try:
        db.session.commit()
        click.echo("Successfully seeded Maelle's weapons.")
    except Exception as e:
        db.session.rollback()
        click.echo(f"Error seeding Maelle's weapons: {e}")
