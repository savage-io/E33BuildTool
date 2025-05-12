from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models  # Ensure models are imported for Flask-Migrate

    # Register Blueprints
    from app.routes import bp as main_api_bp
    app.register_blueprint(main_api_bp)  # The URL prefix is defined in the blueprint

    from app.seed import seed_maelle_character_command
    from app.seed import seed_weapons_command
    from app.seed import seed_maelle_skills_command
    from app.seed import seed_pictos_luminas_command

    # Register your CLI commands
    app.cli.add_command(seed_maelle_character_command)
    app.cli.add_command(seed_weapons_command)
    app.cli.add_command(seed_maelle_skills_command)
    app.cli.add_command(seed_pictos_luminas_command)

    @app.route('/hello')
    def hello():
        return "Hello, Expedition 33 Tool!"

    return app