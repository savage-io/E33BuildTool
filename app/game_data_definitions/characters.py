from app.game_data_definitions.maelle_skills import MAELLE_SKILL_DEFINITIONS
from app.game_data_definitions.maelle_weapons import MAELLE_WEAPON_DEFINITIONS

# Maelle's character data
MAELLE_CHARACTER_DATA = {
    "name": "Maelle",
    "description": (
        "Maelle is a central playable character in Clair Obscur: Expedition 33, introduced early in the "
        "narrative as a young woman grappling with her place in a world overshadowed by the Paintress. "
        "Orphaned at a young age and fostered by Gustave's family, she joins Expedition 33 viewing it "
        "as an opportunity for self-discovery beyond the confines of Lumière. In combat, Maelle "
        "distinguishes herself as a versatile duelist wielding a rapier, defined by a unique "
        "stance-switching mechanic that dictates her effectiveness and role within the party."
    ),
    "base_stats_json": {
        "HP_Base": 100,
        "Attack_Base": 10,
        "Defense_Base": 10,
        "Speed_Base": 8,
        "AP_Start": 3,
        "AP_Max": 10,
        "LuminaPoints_Base": 5
    },
    "unique_mechanic_description": (
        "Maelle's combat identity revolves around her three distinct stances: Defensive, Offensive, and "
        "Virtuose. Unlike other characters, her effectiveness is directly tied to which stance she currently "
        "occupies, influencing her damage output, defensive capabilities, and even AP generation. She "
        "can also be in a neutral 'Stanceless' state, which offers no inherent benefits. "
        "Mastering Maelle requires actively managing these stances. Entering any of the three main "
        "stances grants Maelle 1 Action Point (AP), rewarding players for fluidly transitioning between "
        "them. Skills are the primary method for changing stances... Basic attacks also interact with stances..."
    ),
    "icon_url": "/static/images/characters/maelle_portrait.png",
    "skills": MAELLE_SKILL_DEFINITIONS,
    "weapons": MAELLE_WEAPON_DEFINITIONS
}

CHARACTER_DEFINITIONS = [
    MAELLE_CHARACTER_DATA
]
