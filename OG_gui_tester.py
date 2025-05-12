import sys
import os
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QComboBox
)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from app.game_data_definitions.characters import CHARACTER_DEFINITIONS
from app.game_data_definitions.maelle_weapons import MAELLE_WEAPON_DEFINITIONS
from app.game_data_definitions.picto_lumina import PICTOS_LUMINAS_DEFINITIONS

class DataManagementTool(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Initializing Data Management Tool...")
        self.setWindowTitle("Data Management Tool")
        self.setGeometry(100, 100, 800, 600)

        # Create the tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add user preference for maximum act completed
        self.user_max_act = 99  # Default to 'Show All Content'
        self.add_user_preferences_tab()

        # Add character-specific tabs
        print("Adding character-specific tabs...")
        self.add_character_tabs()
        print("Character-specific tabs added.")

        print("Adding picto tab...")
        self.add_picto_tab()
        print("Picto tab added.")

    def add_user_preferences_tab(self):
        """Add a tab for user preferences to set maximum act completed."""
        preferences_tab = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("User Preferences"))

        # Dropdown for selecting maximum act completed
        self.act_dropdown = QComboBox()
        self.act_dropdown.addItem("Show All Content")
        self.act_dropdown.addItem("Act 1 Content Only")
        self.act_dropdown.addItem("Show Act 2 Content")
        self.act_dropdown.currentIndexChanged.connect(self.update_user_max_act)
        layout.addWidget(self.act_dropdown)

        preferences_tab.setLayout(layout)
        self.tabs.addTab(preferences_tab, "Preferences")

    def update_user_max_act(self):
        """Update the user_max_act based on dropdown selection."""
        selected_index = self.act_dropdown.currentIndex()
        if selected_index == 0:
            self.user_max_act = 99  # Show All Content
        elif selected_index == 1:
            self.user_max_act = 1  # Act 1 Content Only
        elif selected_index == 2:
            self.user_max_act = 2  # Show Act 2 Content

        # Refresh character tabs to apply the new filter
        self.refresh_character_tabs()

    def refresh_character_tabs(self):
        """Refresh character tabs to apply filtering based on user_max_act."""
        self.tabs.clear()
        self.add_user_preferences_tab()
        self.add_character_tabs()
        self.add_picto_tab()

    def add_character_tabs(self):
        print("Loading CHARACTER_DEFINITIONS...")
        for character in CHARACTER_DEFINITIONS:
            print(f"Loaded character: {character['name']}")
            character_tab = QWidget()
            character_layout = QVBoxLayout()

            character_layout.addWidget(QLabel(f"{character['name']} Data Management"))

            # Create sub-tabs for weapons and skills
            sub_tabs = QTabWidget()

            # Weapons tab
            weapons_tab = QWidget()
            weapons_layout = QVBoxLayout()

            if character['name'] == "Maelle":
                print("Adding weapons for Maelle...")
                weapons_dropdown = QComboBox()
                weapon_details_label = QLabel("Select a weapon to see details.")
                weapons_layout.addWidget(weapons_dropdown)
                weapons_layout.addWidget(weapon_details_label)

                for weapon in MAELLE_WEAPON_DEFINITIONS:
                    weapons_dropdown.addItem(weapon['name'])

                def update_weapon_details(index):
                    if index >= 0:
                        weapon = MAELLE_WEAPON_DEFINITIONS[index]
                        details = f"Name: {weapon['name']}\n"
                        if 'power_by_level' in weapon:
                            max_power = max(weapon['power_by_level'].values())
                            details += f"Max Power: {max_power}\n"
                        if 'element' in weapon:
                            details += f"Element: {weapon['element']}\n"
                        if 'attribute_scaling' in weapon:
                            details += "Attribute Scaling:\n"
                            for attr, scaling in weapon['attribute_scaling'].items():
                                details += f"  {attr}: {scaling}\n"
                        weapon_details_label.setText(details)

                weapons_dropdown.currentIndexChanged.connect(update_weapon_details)

            weapons_tab.setLayout(weapons_layout)
            sub_tabs.addTab(weapons_tab, "Weapons")

            # Skills tab
            skills_tab = QWidget()
            skills_layout = QVBoxLayout()

            skills_dropdown = QComboBox()
            skill_details_label = QLabel("Select a skill to see details.")
            skills_layout.addWidget(skills_dropdown)
            skills_layout.addWidget(skill_details_label)

            allowed_skills = self.filter_skills(character.get('skills', []))
            for skill in allowed_skills:
                skills_dropdown.addItem(skill['name'])

            def update_skill_details(index):
                if index >= 0:
                    skill = allowed_skills[index]
                    details = f"Name: {skill['name']}\nDescription: {skill['description']}\nAP Cost: {skill['ap_cost']}\nTags: {', '.join(skill['tags_json'])}"
                    skill_details_label.setText(details)

            skills_dropdown.currentIndexChanged.connect(update_skill_details)

            skills_tab.setLayout(skills_layout)
            sub_tabs.addTab(skills_tab, "Skills")

            character_layout.addWidget(sub_tabs)
            character_tab.setLayout(character_layout)
            self.tabs.addTab(character_tab, character['name'])

    def filter_skills(self, skills):
        """Filter skills based on user_max_act."""
        allowed_skills = []
        for skill in skills:
            spoiler_info = skill.get('spoiler_info_json')
            if spoiler_info is None:
                allowed_skills.append(skill)
                continue

            act_available = spoiler_info.get("act_available")
            if act_available is None:
                allowed_skills.append(skill)
                continue

            try:
                if int(act_available) <= self.user_max_act:
                    allowed_skills.append(skill)
            except ValueError:
                print(f"Warning: Non-integer act_available for skill {skill['name']}: {act_available}")
                allowed_skills.append(skill)

        return allowed_skills

    def add_picto_tab(self):
        print("Adding Pictos tab...")
        picto_tab = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Pictos Data Management"))

        picto_dropdown = QComboBox()
        picto_details_label = QLabel("Select a Picto/Lumina to see details.")
        layout.addWidget(picto_dropdown)
        layout.addWidget(picto_details_label)

        if PICTOS_LUMINAS_DEFINITIONS:
            for picto in PICTOS_LUMINAS_DEFINITIONS:
                picto_dropdown.addItem(picto['name'])

            def update_picto_details(index):
                if index >= 0:
                    picto = PICTOS_LUMINAS_DEFINITIONS[index]
                    details = f"Name: {picto['name']}\nDescription: {picto['lumina_description']}\nLP Cost: {picto['lumina_lp_cost']}\nType: {picto['lumina_type']}\nTags: {', '.join(picto['tags_json'])}"
                    picto_details_label.setText(details)

            picto_dropdown.currentIndexChanged.connect(update_picto_details)
        else:
            picto_dropdown.addItem("No pictos data available.")

        picto_tab.setLayout(layout)
        self.tabs.addTab(picto_tab, "Pictos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataManagementTool()
    window.show()
    sys.exit(app.exec_())
