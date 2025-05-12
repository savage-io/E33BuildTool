from app import create_app, db
from app.models import User, GameCharacterCOE33, SkillCOE33, PictoLumina, UserBuildCOE33  # Updated imports

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)