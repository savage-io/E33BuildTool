from app import db, create_app
from app.models import GameCharacterCOE33

def inspect_characters():
    app = create_app()
    with app.app_context():
        try:
            characters = GameCharacterCOE33.query.all()
            if not characters:
                print("No characters found in the database.")
            else:
                for char in characters:
                    print(f"Name: {char.name}, Description: {char.description}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    inspect_characters()
