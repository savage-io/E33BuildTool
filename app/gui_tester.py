import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config

# Database connection setup
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
inspector = inspect(engine)

# GUI setup
class DatabaseInspectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Inspector")

        # Table selection
        self.table_label = tk.Label(root, text="Select a Table:")
        self.table_label.pack(pady=5)

        self.table_combobox = ttk.Combobox(root, values=inspector.get_table_names())
        self.table_combobox.pack(pady=5)
        self.table_combobox.bind("<<ComboboxSelected>>", self.display_table_info)

        # Table info display
        self.info_text = tk.Text(root, wrap=tk.WORD, height=20, width=80)
        self.info_text.pack(pady=10)

    def display_table_info(self, event):
        table_name = self.table_combobox.get()
        if not table_name:
            messagebox.showerror("Error", "Please select a table.")
            return

        # Clear previous info
        self.info_text.delete(1.0, tk.END)

        # Display columns
        self.info_text.insert(tk.END, f"Columns in {table_name}:\n")
        columns = inspector.get_columns(table_name)
        for column in columns:
            self.info_text.insert(tk.END, f"- {column['name']} ({column['type']})\n")

        # Display row count
        try:
            row_count = session.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
            self.info_text.insert(tk.END, f"\nRow count: {row_count}\n")
        except Exception as e:
            self.info_text.insert(tk.END, f"\nError fetching row count: {e}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseInspectorApp(root)
    root.mainloop()
