import click
from flask.cli import with_appcontext
from . import db
from .models import GameCharacterCOE33
from .game_data_definitions.characters import MAELLE_CHARACTER_DATA

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
