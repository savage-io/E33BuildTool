import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
)
from app.game_data_definitions.characters import CHARACTER_DEFINITIONS
from app.game_data_definitions.maelle_weapons import MAELLE_WEAPON_DEFINITIONS

class DataManagementTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Management Tool")
        self.setGeometry(100, 100, 800, 600)

        # Create the tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add character-specific tabs
        self.add_character_tabs()
        self.add_picto_tab()

    def add_character_tabs(self):
        for character in CHARACTER_DEFINITIONS:
            character_tab = QWidget()
            layout = QVBoxLayout()

            layout.addWidget(QLabel(f"{character['name']} Data Management"))

            # Add existing weapons list if character is Maelle
            if character['name'] == "Maelle":
                layout.addWidget(QLabel("Existing Weapons:"))
                for weapon in MAELLE_WEAPON_DEFINITIONS:
                    layout.addWidget(QLabel(f"- {weapon['name']}: {weapon['power']} Power"))

                # Add download CSV button
                download_button = QPushButton("Download Weapons CSV Template")
                download_button.clicked.connect(self.download_csv_template)
                layout.addWidget(download_button)

            # Add upload buttons for weapons and skills
            upload_weapons_button = QPushButton(f"Upload {character['name']} Weapons Data")
            upload_weapons_button.clicked.connect(lambda: self.upload_file(character['name'], "weapons"))
            layout.addWidget(upload_weapons_button)

            upload_skills_button = QPushButton(f"Upload {character['name']} Skills Data")
            upload_skills_button.clicked.connect(lambda: self.upload_file(character['name'], "skills"))
            layout.addWidget(upload_skills_button)

            character_tab.setLayout(layout)
            self.tabs.addTab(character_tab, character['name'])

    def add_picto_tab(self):
        picto_tab = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Pictos Data Management"))

        # Add upload button
        upload_button = QPushButton("Upload Pictos Data")
        upload_button.clicked.connect(self.upload_file)
        layout.addWidget(upload_button)

        picto_tab.setLayout(layout)
        self.tabs.addTab(picto_tab, "Pictos")

    def upload_file(self, character_name=None, data_type=None):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv);;Excel Files (*.xlsx)", options=options)
        if file_path:
            print(f"File selected for {character_name} ({data_type}): {file_path}")

    def download_csv_template(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV Template", "weapons_template.csv", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write headers for the CSV template
                writer.writerow(["name", "element", "power", "attributes", "passive_effects", "acquisition", "stance_synergy", "element_interactions", "power_scaling", "attribute_scaling", "max_level"])
                # Example row
                writer.writerow(["Example Weapon", "Physical", 1000, "{\"Vitality\": \"C\"}", "{\"lvl_4\": \"N/A\"}", "Starting Weapon", "[]", "{}", "{\"base\": 1000, \"max\": 3228}", "{\"Vitality\": {\"base\": \"C\", \"max\": \"S\"}}", 33])
            print(f"CSV template saved to {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataManagementTool()
    window.show()
    sys.exit(app.exec_())
