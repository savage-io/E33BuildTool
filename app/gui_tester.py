import sys
import os
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QComboBox
)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
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
            character_layout = QVBoxLayout()

            character_layout.addWidget(QLabel(f"{character['name']} Data Management"))

            # Create sub-tabs for weapons and skills
            sub_tabs = QTabWidget()

            # Weapons tab
            weapons_tab = QWidget()
            weapons_layout = QVBoxLayout()

            if character['name'] == "Maelle":
                weapons_layout.addWidget(QLabel("Existing Weapons:"))
                for weapon in MAELLE_WEAPON_DEFINITIONS:
                    weapon_dropdown = QComboBox()
                    weapon_dropdown.addItem(f"{weapon['name']}")
                    if 'power_by_level' in weapon:
                        max_power = max(weapon['power_by_level'].values())
                        weapon_dropdown.addItem(f"Max Power: {max_power}")
                    else:
                        weapon_dropdown.addItem("Power data not available")

                    # Add additional attributes
                    if 'element' in weapon:
                        weapon_dropdown.addItem(f"Element: {weapon['element']}")

                    if 'power_by_level' in weapon:
                        weapon_dropdown.addItem("Power by Level:")
                        for level, power in weapon['power_by_level'].items():
                            weapon_dropdown.addItem(f"  Level {level}: {power}")

                    if 'attribute_scaling' in weapon:
                        weapon_dropdown.addItem("Attribute Scaling:")
                        for attr, scaling in weapon['attribute_scaling'].items():
                            weapon_dropdown.addItem(f"  {attr}: {scaling}")

                    weapons_layout.addWidget(weapon_dropdown)

            weapons_tab.setLayout(weapons_layout)
            sub_tabs.addTab(weapons_tab, "Weapons")

            # Skills tab
            skills_tab = QWidget()
            skills_layout = QVBoxLayout()

            skills_layout.addWidget(QLabel("Existing Skills:"))
            for skill in character.get('skills', []):
                skill_dropdown = QComboBox()
                skill_dropdown.addItem(f"{skill['name']}")
                skill_dropdown.addItem(f"Description: {skill['description']}")
                skills_layout.addWidget(skill_dropdown)

            skills_tab.setLayout(skills_layout)
            sub_tabs.addTab(skills_tab, "Skills")

            character_layout.addWidget(sub_tabs)
            character_tab.setLayout(character_layout)
            self.tabs.addTab(character_tab, character['name'])

    def add_picto_tab(self):
        picto_tab = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Pictos Data Management"))

        # Placeholder dropdown for pictos data
        picto_dropdown = QComboBox()
        picto_dropdown.addItem("No pictos data available.")
        layout.addWidget(picto_dropdown)

        picto_tab.setLayout(layout)
        self.tabs.addTab(picto_tab, "Pictos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataManagementTool()
    window.show()
    sys.exit(app.exec_())
