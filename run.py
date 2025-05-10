from app import create_app, db
from app.models import User, GameCharacterCOE33, SkillCOE33, PictoCOE33, LuminaCOE33, UserBuildCOE33

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)