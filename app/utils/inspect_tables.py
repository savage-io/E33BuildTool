from sqlalchemy import create_engine, inspect

def list_tables():
    engine = create_engine('sqlite:///app.db')
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the database:")
    for table in tables:
        print(table)

if __name__ == "__main__":
    list_tables()
