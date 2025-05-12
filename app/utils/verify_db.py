from app import db, create_app
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from sqlalchemy import inspect, text  # Add this import for table inspection and raw SQL execution

def verify_database():
    try:
        app = create_app()
        with app.app_context():
            # Check if the database connection is working
            connection = db.engine.connect()
            print("Database connection successful.")

            # List all tables in the database
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print("Tables in the database:", tables)

            connection.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def backup_tables():
    try:
        app = create_app()
        with app.app_context():
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

            with db.engine.connect() as connection:
                for table in tables:
                    if table == 'alembic_version':
                        continue  # Skip Alembic-related tables
                    backup_table_name = f"{table}_backup_{timestamp}"
                    connection.execute(text(f"CREATE TABLE {backup_table_name} AS SELECT * FROM {table};"))
                    print(f"Backed up table: {table} to {backup_table_name}.")

    except SQLAlchemyError as e:
        print(f"An error occurred while backing up tables: {e}")

# Removed references to luminas_coe33
def drop_old_tables(connection):
    connection.execute(text("DROP TABLE IF EXISTS pictos_coe33;"))
    print("Dropped old table: pictos_coe33.")

def update_database():
    try:
        app = create_app()
        with app.app_context():
            with db.engine.connect() as connection:
                drop_old_tables(connection)

            # Create new table
            db.create_all()
            print("Created new table: PictoLumina.")

    except SQLAlchemyError as e:
        print(f"An error occurred while updating the database: {e}")

if __name__ == "__main__":
    print("Verifying database...")
    verify_database()
    print("Backing up all tables...")
    backup_tables()
    print("Updating database schema...")
    update_database()
