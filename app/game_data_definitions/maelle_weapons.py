from app.utils.weapon_utils import calculate_weapon_stats

# Maelle's weapon data
# Note: All attributes, including stance changes, elements, and upgrade scaling, are tracked for implementations of the recommendation system.
MAELLE_WEAPON_DEFINITIONS = [
    {
        "name": "Maellum",
        "element": "Physical",
        "power": 3228,
        "attributes": {"Vitality": "S"},
        "passive_effects": {
            "lvl_4": "N/A",
            "lvl_10": "N/A",
            "lvl_20": "N/A"
        },
        "acquisition": "Starting Weapon",
        "stance_synergy": [],
        "element_interactions": {},
        "power_scaling": {"base": 1000, "max": 3228},  # Base power at level 1 and max power at level 33
        "attribute_scaling": {"Vitality": {"base": "C", "max": "S"}},  # Scaling of attributes from level 1 to 33
        "max_level": 33  # Maximum upgrade level
    },
    {
        "name": "Barrier Breaker",
        "element": "Void",
        "power": 3713,
        "attributes": {"Defense": "S", "Agility": "A"},
        "passive_effects": {
            "lvl_4": "Steal Shields removed by hitting enemies.",
            "lvl_10": "Switch to Virtuose Stance on breaking any Shield.",
            "lvl_20": "Hitting a Marked enemy breaks all its Shields."
        },
        "acquisition": "Main Quest Item",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Void": "Breaks Shields"},
        "power_scaling": {"base": 1200, "max": 3713},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Agility": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Battlum",
        "element": "Physical",
        "power": 3035,
        "attributes": {"Defense": "S", "Luck": "A"},
        "passive_effects": {
            "lvl_4": "Double Gradient generation while in Defensive Stance.",
            "lvl_10": "If Stanceless, Base Attack switches to Defensive Stance.",
            "lvl_20": "+5% of a Gradient Charge on Parry."
        },
        "acquisition": "Falling Leaves",
        "stance_synergy": ["Defensive"],
        "element_interactions": {},
        "power_scaling": {"base": 1000, "max": 3035},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Luck": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Brulerum",
        "element": "Fire",
        "power": 2744,
        "attributes": {"Agility": "A", "Luck": "S"},
        "passive_effects": {
            "lvl_4": "Critical hits apply Burn.",
            "lvl_10": "Base Attack applies 2 Burn.",
            "lvl_20": "100% Critical Chance while Stanceless."
        },
        "acquisition": "Flying Waters (Bruler drop near Noco's Hut) al Cave (Bruler merchant purchase)",
        "stance_synergy": [],
        "element_interactions": {"Fire": "Applies Burn"},
        "power_scaling": {"base": 900, "max": 2744},
        "attribute_scaling": {"Agility": {"base": "C", "max": "A"}, "Luck": {"base": "B", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Chalium",
        "element": "Light",
        "power": 3422,
        "attributes": {"Vitality": "A", "Agility": "S"},
        "passive_effects": {
            "lvl_4": "On Defensive Stance, gain 1 Shield per Parry. Lose all Shields on turn start.",
            "lvl_10": "20% increased Light damage with Skills.",
            "lvl_20": "50% increased Counter damage per Shield."
        },
        "acquisition": "Sinister Cave (Chromatic Chalier drop)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Light": "Increased damage with Skills"},
        "power_scaling": {"base": 1100, "max": 3422},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "A"}, "Agility": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Chantenum",
        "element": "Fire",
        "power": 2841,
        "attributes": {"Agility": "A", "Luck": "S"},
        "passive_effects": {
            "lvl_4": "On turn start, if Stanceless, switch to Offensive Stance.",
            "lvl_10": "Fire Skills cost 1 less AP.",
            "lvl_20": "+1 Shield on switching to Offensive Stance."
        },
        "acquisition": "Sirene (Klaudiso merchant purchase after duel)",
        "stance_synergy": ["Offensive"],
        "element_interactions": {"Fire": "Reduced AP cost for Skills"},
        "power_scaling": {"base": 900, "max": 2841},
        "attribute_scaling": {"Agility": {"base": "C", "max": "A"}, "Luck": {"base": "B", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Clierum",
        "element": "Lightning",
        "power": 3422,
        "attributes": {"Defense": "A", "Agility": "S"},
        "passive_effects": {
            "lvl_4": "Critical hits with skills give 2 AP. Once per turn.",
            "lvl_10": "20% increased Lightning damage with skills.",
            "lvl_20": "+50% Critical Chance while in Offensive Stance."
        },
        "acquisition": "Visages (Seething Bouchelier drop)",
        "stance_synergy": ["Offensive"],
        "element_interactions": {"Lightning": "Increased damage with Skills"},
        "power_scaling": {"base": 1100, "max": 3422},
        "attribute_scaling": {"Defense": {"base": "B", "max": "A"}, "Agility": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Coldum",
        "element": "Ice",
        "power": 2583,
        "attributes": {"Vitality": "S", "Defense": "A"},
        "passive_effects": {
            "lvl_4": "Self-Heal by 2% Health on dealing a Critical hit.",
            "lvl_10": "+50% Critical Chance while in Defensive Stance.",
            "lvl_20": "If Stanceless, Base Attack switches to Defensive Stance."
        },
        "acquisition": "Monoco's Station (Grandis merchant purchase after Eternal Ice quest)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Ice": "Self-Heal on Critical hit"},
        "power_scaling": {"base": 800, "max": 2583},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "S"}, "Defense": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Duenum",
        "element": "Physical",
        "power": 2421,
        "attributes": {"Defense": "S", "Agility": "A"},
        "passive_effects": {
            "lvl_4": "In Defensive Stance, gaining AP also gives 1 AP to allies.",
            "lvl_10": "If Stanceless, Base Attack switches to Defensive Stance.",
            "lvl_20": "+1 AP on Stance switch."
        },
        "acquisition": "Stone Wave Cliffs (Paint Cage near Farm Waypoint)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {},
        "power_scaling": {"base": 800, "max": 2421},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Agility": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Facesum",
        "element": "Physical",
        "power": 3293,
        "attributes": {"Vitality": "A", "Luck": "S"},
        "passive_effects": {
            "lvl_4": "In Offensive Stance, double the amount of Burn applied.",
            "lvl_10": "50% increased Burn damage.",
            "lvl_20": "Base Attack propagates Burn."
        },
        "acquisition": "Isle of the Eyes",
        "stance_synergy": ["Offensive"],
        "element_interactions": {"Fire": "Increased Burn damage"},
        "power_scaling": {"base": 1000, "max": 3293},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "A"}, "Luck": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Glaisum",
        "element": "Physical",
        "power": 3713,
        "attributes": {"Defense": "S", "Agility": "A"},
        "passive_effects": {
            "lvl_4": "Allies recover 20% Health on switching to Virtuose Stance.",
            "lvl_10": "Gain Shell when switching out of Virtuose Stance.",
            "lvl_20": "Cleanse self Status Effects when switching to Virtuose Stance."
        },
        "acquisition": "Falling Leaves (Glaise drop in Resinveil Grove)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "power_scaling": {"base": 1200, "max": 3713},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Agility": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Jarum",
        "element": "Physical",
        "power": 2583,
        "attributes": {"Defense": "S", "Luck": "A"},
        "passive_effects": {
            "lvl_4": "Switch to Virtuose Stance on Counterattack.",
            "lvl_10": "Apply 5 Burn on Counterattack.",
            "lvl_20": "50% increased Counter damage per Shield."
        },
        "acquisition": "The Continent (Chromatic Jar boss drop west of Gestral Village)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Fire": "Apply Burn on Counterattack"},
        "power_scaling": {"base": 800, "max": 2583},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Luck": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Lithum",
        "element": "Void",
        "power": 3228,
        "attributes": {"Agility": "A", "Luck": "S"},
        "passive_effects": {
            "lvl_4": "In Virtuose Stance, hitting a Marked enemy doesn't remove Mark.",
            "lvl_10": "Switch to Virtuose Stance on Counterattack.",
            "lvl_20": "Gain Shell when switching out of Virtuose Stance."
        },
        "acquisition": "The Reacher (Alicia drop, requires Maelle Relationship Level 5+)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Void": "Hitting Marked enemy doesn't remove Mark"},
        "power_scaling": {"base": 1000, "max": 3228},
        "attribute_scaling": {"Agility": {"base": "C", "max": "A"}, "Luck": {"base": "B", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Medalum",
        "element": "Physical",
        "power": 3713,
        "attributes": {"Defense": "S", "Agility": "A"},
        "passive_effects": {
            "lvl_4": "Start in Virtuose Stance.",
            "lvl_10": "In Virtuose Stance, every Burn applied is doubled.",
            "lvl_20": "In Virtuose Stance, Burn deals double damage."
        },
        "acquisition": "Gestral Village (Tournament Reward if Maelle wins final fight)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Fire": "Burn deals double damage"},
        "power_scaling": {"base": 1200, "max": 3713},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Agility": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Melarum",
        "element": "Physical",
        "power": 3293,
        "attributes": {"Vitality": "S", "Luck": "A"},
        "passive_effects": {
            "lvl_4": "Allies recover 20% Health on switching to Virtuose Stance.",
            "lvl_10": "Apply Shell when Health is above 80%.",
            "lvl_20": "Switch to Virtuose Stance when Health falls below 50%."
        },
        "acquisition": "Old Lumiere",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "power_scaling": {"base": 1000, "max": 3293},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "S"}, "Luck": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Plenum",
        "element": "Ice",
        "power": 3035,
        "attributes": {"Defense": "A", "Luck": "S"},
        "passive_effects": {
            "lvl_4": "On turn start, if Stanceless, switch to Defensive Stance.",
            "lvl_10": "In Defensive Stance, double Break damage.",
            "lvl_20": "Support Skills cost 1 less AP."
        },
        "acquisition": "Yellow Harvest (Glaise drop in Yellow Spire Wrecks)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Ice": "Double Break damage"},
        "power_scaling": {"base": 1000, "max": 3035},
        "attribute_scaling": {"Defense": {"base": "B", "max": "A"}, "Luck": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Seashellum",
        "element": "Fire",
        "power": 3422,
        "attributes": {"Defense": "A", "Agility": "S"},
        "passive_effects": {
            "lvl_4": "On Defensive Stance, gain 1 Shield per Parry. Lose all Shields on turn start.",
            "lvl_10": "On applying Shields, also give 1 AP.",
            "lvl_20": "50% increased Counter damage per Shield."
        },
        "acquisition": "Flying Manor",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Fire": "Increased Counter damage per Shield"},
        "power_scaling": {"base": 1100, "max": 3422},
        "attribute_scaling": {"Defense": {"base": "B", "max": "A"}, "Agility": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Sekarum",
        "element": "Physical",
        "power": 3390,
        "attributes": {"Vitality": "S", "Agility": "A"},
        "passive_effects": {
            "lvl_4": "Switch to Virtuose Stance on breaking any Shield.",
            "lvl_10": "Free Aim shots break 2 shields.",
            "lvl_20": "In Virtuose Stance, all damage pierce Shields."
        },
        "acquisition": "Gestral Village (Eesda merchant purchase after duel)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "power_scaling": {"base": 1100, "max": 3390},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "S"}, "Agility": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Stalum",
        "element": "Fire",
        "power": 3228,
        "attributes": {"Defense": "S", "Luck": "A"},
        "passive_effects": {
            "lvl_4": "Apply Burn on self on turn start. 10% increased damage for each self Burn stack.",
            "lvl_10": "Base Attack applies 2 Burn.",
            "lvl_20": "While in Defensive Stance, receive Heal instead of Burn damage."
        },
        "acquisition": "The Continent (Enemy drop) n Hearts (Enemy drop)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Fire": "Increased damage for each self Burn stack"},
        "power_scaling": {"base": 1000, "max": 3228},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Luck": {"base": "C", "max": "A"}},
        "max_level": 33
    },
    {
        "name": "Tissenum",
        "element": "Earth",
        "power": 3874,
        "attributes": {"Vitality": "A", "Agility": "S"},
        "passive_effects": {
            "lvl_4": "In Defensive Stance, double Break damage.",
            "lvl_10": "Gain 9 AP on Breaking an enemy.",
            "lvl_20": "Breaking an enemy deals 3 high amount of Earth damage."
        },
        "acquisition": "Sirene (Tisseur drop)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Earth": "Double Break damage"},
        "power_scaling": {"base": 1200, "max": 3874},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "A"}, "Agility": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Veremum",
        "element": "Physical",
        "power": 3293,
        "attributes": {"Vitality": "A", "Luck": "S"},
        "passive_effects": {
            "lvl_4": "If Stanceless, Base Attack switches to Offensive Stance.",
            "lvl_10": "Counterattacks apply Defenceless.",
            "lvl_20": "+50% Critical Chance while in Offensive Stance."
        },
        "acquisition": "Inside the Monolith (Mistra drop)",
        "stance_synergy": ["Offensive"],
        "element_interactions": {},
        "power_scaling": {"base": 1000, "max": 3293},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "A"}, "Luck": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Volesterum",
        "element": "Physical",
        "power": 3293,
        "attributes": {"Vitality": "A", "Agility": "S"},
        "passive_effects": {
            "lvl_4": "+1 AP on Stance switch.",
            "lvl_10": "If Stanceless, Base Attack switches to Defensive Stance.",
            "lvl_20": "Recover 5% Health on Stance switch."
        },
        "acquisition": "Lumiere (Act 3, Cribappa merchant purchase)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {},
        "power_scaling": {"base": 1000, "max": 3293},
        "attribute_scaling": {"Vitality": {"base": "B", "max": "A"}, "Agility": {"base": "C", "max": "S"}},
        "max_level": 33
    },
    {
        "name": "Yeverum",
        "element": "Physical",
        "power": 3358,
        "attributes": {"Defense": "S", "Agility": "A"},
        "passive_effects": {
            "lvl_4": "Applying Shell also applies 1 Shield.",
            "lvl_10": "On applying Shields, also give 1 AP.",
            "lvl_20": "On switching to Virtuose Stance, double all Shields on allies."
        },
        "acquisition": "Renoir's Drafts (Grour merchant purchase after duel)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "power_scaling": {"base": 1000, "max": 3358},
        "attribute_scaling": {"Defense": {"base": "B", "max": "S"}, "Agility": {"base": "C", "max": "A"}},
        "max_level": 33
    }
]

# Placeholder for Maelle's weapon comparison table
# The table will be populated with detailed weapon data later.
