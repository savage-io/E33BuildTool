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

    @app.route('/hello')
    def hello():
        return "Hello, Expedition 33 Tool!"

    return app