from app import db, create_app

def verify_database():
    try:
        app = create_app()
        with app.app_context():
            # Check if the database connection is working
            connection = db.engine.connect()
            print("Database connection successful.")

            # List all tables in the database
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print("Tables in the database:", tables)

            connection.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    verify_database()
