from app.utils.weapon_utils import calculate_weapon_stats

# Maelle's weapon data
# Note: All attributes, including stance changes, elements, and upgrade scaling, are tracked for implementations of the recommendation system.
MAELLE_WEAPON_DEFINITIONS = [
    {
        "name": "Barrier Breaker",
        "element": "Void",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 2},
        "power at max level": 3616,
        "attributes": ["Defense", "Agility"],
        "power_by_level": {"1": 51, "2": 77, "3": 102, "4": 136, "5": 186, "6": 237, "7": 287, "8": 338, "9": 388, "10": 470, "11": 548, "12": 627, "13": 705, "14": 783, "15": 862, "16": 940, "17": 1019, "18": 1097, "19": 1175, "20": 1345, "21": 1460, "22": 1575, "23": 1691, "24": 1806, "25": 1921, "26": 2037, "27": 2152, "28": 2267, "29": 2383, "30": 2498, "31": 2613, "32": 2729, "33": 3616},
        "attribute_scaling_tiers": {"Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Steal Shields removed by hitting enemies.",
                "tags": ["Trigger:OnHit", "Effect:StealShields", "Synergy:ShieldBreak"]
            },
            "lvl_10": {
                "description": "Switch to Virtuose Stance on breaking any Shield.",
                "tags": ["Trigger:OnShieldBreak", "Effect:StanceSwitch", "Stance:Virtuose"]
            },
            "lvl_20": {
                "description": "Hitting a Marked enemy breaks all its Shields.",
                "tags": ["Trigger:OnHitMarked", "Effect:BreakAllShields", "Synergy:MarkedTargets"]
            }
        },
        "acquisition_info": "Main Quest Item",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Void": "Breaks Shields"},
        "max_level": 33
    },
    {
        "name": "Battlum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3067,
        "attributes": ["Luck", "Defense"],
        "power_by_level": {"1": 43, "2": 65, "3": 87, "4": 115, "5": 158, "6": 201, "7": 244, "8": 286, "9": 329, "10": 399, "11": 465, "12": 532, "13": 598, "14": 665, "15": 731, "16": 798, "17": 864, "18": 931, "19": 997, "20": 1140, "21": 1238, "22": 1336, "23": 1434, "24": 1532, "25": 1630, "26": 1728, "27": 1825, "28": 1923, "29": 2021, "30": 2119, "31": 2217, "32": 2315, "33": 3067},
        "attribute_scaling_tiers": {"Luck": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Double Gradient generation while in Defensive Stance.",
                "tags": ["Trigger:InDefensiveStance", "Effect:DoubleGradientGeneration", "Synergy:DefensiveBuild"]
            },
            "lvl_10": {
                "description": "If Stanceless, Base Attack switches to Defensive Stance.",
                "tags": ["Condition:Stanceless", "Effect:StanceSwitch", "Stance:Defensive"]
            },
            "lvl_20": {
                "description": "+5% of a Gradient Charge on Parry.",
                "tags": ["Trigger:OnParry", "Effect:GradientChargeGain", "Value:0.05"]
            }
        },
        "acquisition_info": "Falling Leaves",
        "stance_synergy": ["Defensive"],
        "element_interactions": {},
        "max_level": 33
    },
    {
        "name": "Brulerum",
        "element": "Fire",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 2744,
        "attributes": ["Luck", "Agility"],
        "power_by_level": {"1": 39, "2": 58, "3": 78, "4": 103, "5": 142, "6": 180, "7": 218, "8": 256, "9": 295, "10": 357, "11": 416, "12": 476, "13": 535, "14": 595, "15": 654, "16": 714, "17": 773, "18": 833, "19": 892, "20": 1020, "21": 1108, "22": 1196, "23": 1283, "24": 1371, "25": 1458, "26": 1546, "27": 1633, "28": 1721, "29": 1808, "30": 1896, "31": 1984, "32": 2071, "33": 2744},
        "attribute_scaling_tiers": {"Luck": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Critical hits apply Burn.",
                "tags": ["Trigger:OnCrit", "Effect:AppliesStatus", "Status:Burn", "Synergy:BurnBuild"]
            },
            "lvl_10": {
                "description": "Base Attack applies 2 Burn.",
                "tags": ["Trigger:OnBaseAttack", "Effect:AppliesStatus", "Status:Burn", "Stacks:2"]
            },
            "lvl_20": {
                "description": "100% Critical Chance while Stanceless.",
                "tags": ["Condition:Stanceless", "Effect:StatBoost", "Stat:CritChance", "Value:1.0", "Operator:SetTo", "Synergy:CritBuild"]
            }
        },
        "acquisition_info": "Flying Waters (Bruler drop near Noco's Hut) al Cave (Bruler merchant purchase)",
        "stance_synergy": [],
        "element_interactions": {"Fire": "Applies Burn"},
        "max_level": 33
    },
    {
        "name": "Chalium",
        "element": "Light",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3422,
        "attributes": ["Vitality", "Agility"],
        "power_by_level": {"1": 48, "2": 73, "3": 97, "4": 129, "5": 176, "6": 224, "7": 272, "8": 320, "9": 367, "10": 445, "11": 519, "12": 593, "13": 667, "14": 741, "15": 816, "16": 890, "17": 964, "18": 1038, "19": 1112, "20": 1272, "21": 1382, "22": 1491, "23": 1600, "24": 1709, "25": 1818, "26": 1928, "27": 2037, "28": 2146, "29": 2255, "30": 2364, "31": 2473, "32": 2583, "33": 3422},
        "attribute_scaling_tiers": {"Vitality": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Agility": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "On Defensive Stance, gain 1 Shield per Parry. Lose all Shields on turn start.",
                "tags": ["Trigger:OnParry", "Effect:GainShield", "Value:1", "Condition:InDefensiveStance", "Effect:RemoveAllShields", "Trigger:TurnStart"]
            },
            "lvl_10": {
                "description": "20% increased Light damage with Skills.",
                "tags": ["Effect:DamageBoost", "DamageType:Light", "Value:0.2", "Trigger:OnSkill"]
            },
            "lvl_20": {
                "description": "50% increased Counter damage per Shield.",
                "tags": ["Effect:DamageBoost", "DamageType:Counter", "Value:0.5", "Condition:PerShield"]
            }
        },
        "acquisition_info": "Sinister Cave (Chromatic Chalier drop)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Light": "Increased damage with Skills"},
        "max_level": 33
    },
    {
        "name": "Chantenum",
        "element": "Fire",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 2841,
        "attributes": ["Luck", "Agility"],
        "power_by_level": {"1": 40, "2": 60, "3": 81, "4": 107, "5": 147, "6": 186, "7": 226, "8": 265, "9": 305, "10": 369, "11": 431, "12": 492, "13": 554, "14": 616, "15": 677, "16": 739, "17": 800, "18": 862, "19": 924, "20": 1056, "21": 1147, "22": 1238, "23": 1328, "24": 1419, "25": 1510, "26": 1600, "27": 1691, "28": 1782, "29": 1872, "30": 1963, "31": 2054, "32": 2144, "33": 2841},
        "attribute_scaling_tiers": {"Luck": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "On turn start, if Stanceless, switch to Offensive Stance.",
                "tags": ["Trigger:TurnStart", "Condition:Stanceless", "Effect:StanceSwitch", "Stance:Offensive"]
            },
            "lvl_10": {
                "description": "Fire Skills cost 1 less AP.",
                "tags": ["Trigger:OnSkill", "Condition:FireSkill", "Effect:APCostReduction", "Value:1"]
            },
            "lvl_20": {
                "description": "+1 Shield on switching to Offensive Stance.",
                "tags": ["Trigger:OnStanceSwitch", "Condition:ToOffensiveStance", "Effect:GainShield", "Value:1"]
            }
        },
        "acquisition_info": "Sirene (Klaudiso merchant purchase after duel)",
        "stance_synergy": ["Offensive"],
        "element_interactions": {"Fire": "Reduced AP cost for Skills"},
        "max_level": 33
    },
    {
        "name": "Clierum",
        "element": "Lightning",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3196,
        "attributes": ["Defense", "Agility"],
        "power_by_level": {"1": 45, "2": 68, "3": 91, "4": 120, "5": 165, "6": 209, "7": 254, "8": 298, "9": 343, "10": 415, "11": 485, "12": 554, "13": 623, "14": 693, "15": 762, "16": 831, "17": 900, "18": 970, "19": 1039, "20": 1188, "21": 1290, "22": 1392, "23": 1494, "24": 1596, "25": 1698, "26": 1800, "27": 1902, "28": 2004, "29": 2106, "30": 2208, "31": 2310, "32": 2412, "33": 3196},
        "attribute_scaling_tiers": {"Defense": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Agility": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Critical hits with skills give 2 AP. Once per turn.",
                "tags": ["Trigger:OnCrit", "Condition:Skill", "Effect:APGain", "Value:2", "Limit:OncePerTurn"]
            },
            "lvl_10": {
                "description": "20% increased Lightning damage with skills.",
                "tags": ["Effect:DamageBoost", "DamageType:Lightning", "Value:0.2", "Trigger:OnSkill"]
            },
            "lvl_20": {
                "description": "+50% Critical Chance while in Offensive Stance.",
                "tags": ["Condition:InOffensiveStance", "Effect:StatBoost", "Stat:CritChance", "Value:0.5", "Operator:Add"]
            }
        },
        "acquisition_info": "Visages (Seething Bouchelier drop)",
        "stance_synergy": ["Offensive"],
        "element_interactions": {"Lightning": "Increased damage with Skills"},
        "max_level": 33
    },
    {
        "name": "Coldum",
        "element": "Ice",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 2583,
        "attributes": ["Vitality", "Defense"],
        "power_by_level": {"1": 36, "2": 55, "3": 73, "4": 97, "5": 133, "6": 169, "7": 205, "8": 241, "9": 277, "10": 336, "11": 392, "12": 448, "13": 504, "14": 560, "15": 616, "16": 672, "17": 728, "18": 784, "19": 840, "20": 960, "21": 1043, "22": 1125, "23": 1208, "24": 1290, "25": 1372, "26": 1455, "27": 1537, "28": 1620, "29": 1702, "30": 1784, "31": 1867, "32": 1949, "33": 2583},
        "attribute_scaling_tiers": {"Vitality": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Defense": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Self-Heal by 2% Health on dealing a Critical hit.",
                "tags": ["Trigger:OnCrit", "Effect:SelfHeal", "Value:0.02"]
            },
            "lvl_10": {
                "description": "+50% Critical Chance while in Defensive Stance.",
                "tags": ["Condition:InDefensiveStance", "Effect:StatBoost", "Stat:CritChance", "Value:0.5", "Operator:Add"]
            },
            "lvl_20": {
                "description": "If Stanceless, Base Attack switches to Defensive Stance.",
                "tags": ["Condition:Stanceless", "Effect:StanceSwitch", "Stance:Defensive"]
            }
        },
        "acquisition_info": "Monoco's Station (Grandis merchant purchase after Eternal Ice quest)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Ice": "Self-Heal on Critical hit"},
        "max_level": 33
    },
    {
        "name": "Duenum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 2421,
        "attributes": ["Defense", "Agility"],
        "power_by_level": {"1": 34, "2": 51, "3": 69, "4": 91, "5": 125, "6": 159, "7": 192, "8": 226, "9": 260, "10": 315, "11": 367, "12": 420, "13": 472, "14": 525, "15": 577, "16": 630, "17": 682, "18": 735, "19": 787, "20": 900, "21": 978, "22": 1055, "23": 1132, "24": 1209, "25": 1287, "26": 1364, "27": 1441, "28": 1518, "29": 1596, "30": 1673, "31": 1750, "32": 1827, "33": 2421},
        "attribute_scaling_tiers": {"Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "In Defensive Stance, gaining AP also gives 1 AP to allies.",
                "tags": ["Condition:InDefensiveStance", "Trigger:OnAPGain", "Effect:APGainToAllies", "Value:1"]
            },
            "lvl_10": {
                "description": "If Stanceless, Base Attack switches to Defensive Stance.",
                "tags": ["Condition:Stanceless", "Effect:StanceSwitch", "Stance:Defensive"]
            },
            "lvl_20": {
                "description": "+1 AP on Stance switch.",
                "tags": ["Trigger:OnStanceSwitch", "Effect:APGain", "Value:1"]
            }
        },
        "acquisition_info": "Stone Wave Cliffs (Paint Cage near Farm Waypoint)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {},
        "max_level": 33
    },
    {
        "name": "Facesum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3519,
        "attributes": ["Luck", "Vitality"],
        "power_by_level": {"1": 50, "2": 75, "3": 100, "4": 132, "5": 181, "6": 230, "7": 280, "8": 329, "9": 378, "10": 457, "11": 534, "12": 610, "13": 686, "14": 762, "15": 839, "16": 915, "17": 991, "18": 1068, "19": 1144, "20": 1308, "21": 1421, "22": 1533, "23": 1645, "24": 1758, "25": 1870, "26": 1982, "27": 2094, "28": 2207, "29": 2319, "30": 2431, "31": 2543, "32": 2656, "33": 3519},
        "attribute_scaling_tiers": {"Luck": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Vitality": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "In Offensive Stance, double the amount of Burn applied.",
                "tags": ["Condition:InOffensiveStance", "Effect:DoubleBurnApplication"]
            },
            "lvl_10": {
                "description": "50% increased Burn damage.",
                "tags": ["Effect:DamageBoost", "DamageType:Burn", "Value:0.5"]
            },
            "lvl_20": {
                "description": "Base Attack propagates Burn.",
                "tags": ["Trigger:OnBaseAttack", "Effect:PropagateBurn"]
            }
        },
        "acquisition_info": "Isle of the Eyes",
        "stance_synergy": ["Offensive"],
        "element_interactions": {"Fire": "Increased Burn damage"},
        "max_level": 33
    },
    {
        "name": "Glaisum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3713,
        "attributes": ["Defense", "Agility"],
        "power_by_level": {"1": 52, "2": 79, "3": 105, "4": 140, "5": 191, "6": 243, "7": 295, "8": 347, "9": 398, "10": 482, "11": 563, "12": 643, "13": 724, "14": 804, "15": 885, "16": 965, "17": 1046, "18": 1126, "19": 1207, "20": 1380, "21": 1499, "22": 1617, "23": 1736, "24": 1854, "25": 1973, "26": 2091, "27": 2210, "28": 2328, "29": 2447, "30": 2565, "31": 2683, "32": 2802, "33": 3713},
        "attribute_scaling_tiers": {"Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Allies recover 20% Health on switching to Virtuose Stance.",
                "tags": ["Trigger:OnStanceSwitch", "Condition:ToVirtuoseStance", "Effect:AllyHeal", "Value:0.2"]
            },
            "lvl_10": {
                "description": "Gain Shell when switching out of Virtuose Stance.",
                "tags": ["Trigger:OnStanceSwitch", "Condition:FromVirtuoseStance", "Effect:GainShell"]
            },
            "lvl_20": {
                "description": "Cleanse self Status Effects when switching to Virtuose Stance.",
                "tags": ["Trigger:OnStanceSwitch", "Condition:ToVirtuoseStance", "Effect:SelfCleanse"]
            }
        },
        "acquisition_info": "Falling Leaves (Glaise drop in Resinveil Grove)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "max_level": 33
    },
    {
        "name": "Jarum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 2583,
        "attributes": ["Luck", "Defense"],
        "power_by_level": {"1": 36, "2": 55, "3": 73, "4": 97, "5": 133, "6": 169, "7": 205, "8": 241, "9": 277, "10": 336, "11": 392, "12": 448, "13": 504, "14": 560, "15": 616, "16": 672, "17": 728, "18": 784, "19": 840, "20": 960, "21": 1043, "22": 1125, "23": 1208, "24": 1290, "25": 1372, "26": 1455, "27": 1537, "28": 1620, "29": 1702, "30": 1784, "31": 1867, "32": 1949, "33": 2583},
        "attribute_scaling_tiers": {"Luck": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Switch to Virtuose Stance on Counterattack.",
                "tags": ["Trigger:OnCounterattack", "Effect:StanceSwitch", "Stance:Virtuose"]
            },
            "lvl_10": {
                "description": "Apply 5 Burn on Counterattack.",
                "tags": ["Trigger:OnCounterattack", "Effect:AppliesStatus", "Status:Burn", "Stacks:5"]
            },
            "lvl_20": {
                "description": "50% increased Counter damage per Shield.",
                "tags": ["Effect:DamageBoost", "DamageType:Counter", "Value:0.5", "Condition:PerShield"]
            }
        },
        "acquisition_info": "The Continent (Chromatic Jar boss drop west of Gestral Village)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Fire": "Apply Burn on Counterattack"},
        "max_level": 33
    },
    {
        "name": "Lithum",
        "element": "Void",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3228,
        "attributes": ["Luck", "Agility"],
        "power_by_level": {"1": 45, "2": 68, "3": 91, "4": 121, "5": 166, "6": 211, "7": 256, "8": 301, "9": 346, "10": 419, "11": 489, "12": 559, "13": 629, "14": 699, "15": 769, "16": 839, "17": 909, "18": 979, "19": 1049, "20": 1200, "21": 1303, "22": 1406, "23": 1509, "24": 1612, "25": 1715, "26": 1818, "27": 1921, "28": 2024, "29": 2127, "30": 2230, "31": 2333, "32": 2436, "33": 3228},
        "attribute_scaling_tiers": {"Luck": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "In Virtuose Stance, hitting a Marked enemy doesn't remove Mark.",
                "tags": ["Condition:InVirtuoseStance", "Trigger:OnHitMarked", "Effect:PreserveMark"]
            },
            "lvl_10": {
                "description": "Switch to Virtuose Stance on Counterattack.",
                "tags": ["Trigger:OnCounterattack", "Effect:StanceSwitch", "Stance:Virtuose"]
            },
            "lvl_20": {
                "description": "Gain Shell when switching out of Virtuose Stance.",
                "tags": ["Trigger:OnStanceSwitch", "Condition:FromVirtuoseStance", "Effect:GainShell"]
            }
        },
        "acquisition_info": "The Reacher (Alicia drop, requires Maelle Relationship Level 5+)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Void": "Hitting Marked enemy doesn't remove Mark"},
        "max_level": 33
    },
    {
        "name": "Medalum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 2906,
        "attributes": ["Defense", "Agility"],
        "power_by_level": {"1": 41, "2": 62, "3": 82, "4": 109, "5": 150, "6": 190, "7": 231, "8": 271, "9": 312, "10": 378, "11": 441, "12": 504, "13": 567, "14": 630, "15": 693, "16": 756, "17": 819, "18": 882, "19": 945, "20": 1080, "21": 1173, "22": 1266, "23": 1359, "24": 1451, "25": 1544, "26": 1637, "27": 1729, "28": 1822, "29": 1915, "30": 2007, "31": 2100, "32": 2193, "33": 2906},
        "attribute_scaling_tiers": {"Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Start in Virtuose Stance.",
                "tags": ["Trigger:OnStart", "Effect:StanceSwitch", "Stance:Virtuose"]
            },
            "lvl_10": {
                "description": "In Virtuose Stance, every Burn applied is doubled.",
                "tags": ["Condition:InVirtuoseStance", "Effect:DoubleBurnApplication"]
            },
            "lvl_20": {
                "description": "In Virtuose Stance, Burn deals double damage.",
                "tags": ["Condition:InVirtuoseStance", "Effect:DamageBoost", "DamageType:Burn", "Value:2.0"]
            }
        },
        "acquisition_info": "Gestral Village (Tournament Reward if Maelle wins final fight)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {"Fire": "Burn deals double damage"},
        "max_level": 33
    },
    {
        "name": "Melarum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3584,
        "attributes": ["Luck", "Vitality"],
        "power_by_level": {"1": 50, "2": 76, "3": 102, "4": 135, "5": 185, "6": 235, "7": 285, "8": 335, "9": 385, "10": 466, "11": 543, "12": 621, "13": 699, "14": 776, "15": 854, "16": 932, "17": 1009, "18": 1087, "19": 1165, "20": 1333, "21": 1447, "22": 1561, "23": 1675, "24": 1790, "25": 1904, "26": 2018, "27": 2133, "28": 2247, "29": 2361, "30": 2476, "31": 2590, "32": 2704, "33": 3584},
        "attribute_scaling_tiers": {"Luck": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Vitality": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Allies recover 20% Health on switching to Virtuose Stance.",
                "tags": ["Trigger:OnStanceSwitch", "Condition:ToVirtuoseStance", "Effect:AllyHeal", "Value:0.2"]
            },
            "lvl_10": {
                "description": "Apply Shell when Health is above 80%.",
                "tags": ["Condition:HealthAbove80", "Effect:ApplyShell"]
            },
            "lvl_20": {
                "description": "Switch to Virtuose Stance when Health falls below 50%.",
                "tags": ["Condition:HealthBelow50", "Effect:StanceSwitch", "Stance:Virtuose"]
            }
        },
        "acquisition_info": "Old Lumiere",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "max_level": 33
    },
    {
        "name": "Plenum",
        "element": "Ice",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3035,
        "attributes": ["Luck", "Defense"],
        "power_by_level": {"1": 43, "2": 64, "3": 86, "4": 114, "5": 157, "6": 199, "7": 241, "8": 283, "9": 326, "10": 394, "11": 460, "12": 526, "13": 592, "14": 658, "15": 723, "16": 789, "17": 855, "18": 921, "19": 987, "20": 1128, "21": 1225, "22": 1322, "23": 1419, "24": 1516, "25": 1613, "26": 1709, "27": 1806, "28": 1903, "29": 2000, "30": 2097, "31": 2194, "32": 2290, "33": 3035},
        "attribute_scaling_tiers": {"Luck": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Defense": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "On turn start, if Stanceless, switch to Defensive Stance.",
                "tags": ["Trigger:TurnStart", "Condition:Stanceless", "Effect:StanceSwitch", "Stance:Defensive"]
            },
            "lvl_10": {
                "description": "In Defensive Stance, double Break damage.",
                "tags": ["Condition:InDefensiveStance", "Effect:DamageBoost", "DamageType:Break", "Value:2.0"]
            },
            "lvl_20": {
                "description": "Support Skills cost 1 less AP.",
                "tags": ["Trigger:OnSkill", "Condition:SupportSkill", "Effect:APCostReduction", "Value:1"]
            }
        },
        "acquisition_info": "Yellow Harvest (Glaise drop in Yellow Spire Wrecks)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Ice": "Double Break damage"},
        "max_level": 33
    },
    {
        "name": "Seashelum",
        "element": "Fire",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3003,
        "attributes": ["Agility", "Defense"],
        "power_by_level": {"1": 42, "2": 64, "3": 85, "4": 113, "5": 155, "6": 197, "7": 239, "8": 280, "9": 322, "10": 390, "11": 455, "12": 520, "13": 585, "14": 651, "15": 716, "16": 781, "17": 846, "18": 911, "19": 976, "20": 1116, "21": 1212, "22": 1308, "23": 1404, "24": 1500, "25": 1595, "26": 1691, "27": 1787, "28": 1883, "29": 1979, "30": 2074, "31": 2170, "32": 2266, "33": 3003},
        "attribute_scaling_tiers": {"Agility": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Defense": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "On Defensive Stance, gain 1 Shield per Parry. Lose all Shields on turn start.",
                "tags": ["Trigger:OnParry", "Effect:GainShield", "Value:1", "Condition:InDefensiveStance", "Effect:RemoveAllShields", "Trigger:TurnStart"]
            },
            "lvl_10": {
                "description": "On applying Shields, also give 1 AP.",
                "tags": ["Trigger:OnApplyShield", "Effect:APGain", "Value:1"]
            },
            "lvl_20": {
                "description": "50% increased Counter damage per Shield.",
                "tags": ["Effect:DamageBoost", "DamageType:Counter", "Value:0.5", "Condition:PerShield"]
            }
        },
        "acquisition_info": "Flying Manor",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Fire": "Increased Counter damage per Shield"},
        "max_level": 33
    },
    {
        "name": "Sekarum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3390,
        "attributes": ["Vitality", "Agility"],
        "power_by_level": {"1": 48, "2": 72, "3": 96, "4": 128, "5": 175, "6": 222, "7": 269, "8": 317, "9": 364, "10": 440, "11": 514, "12": 587, "13": 661, "14": 734, "15": 808, "16": 881, "17": 955, "18": 1028, "19": 1102, "20": 1260, "21": 1369, "22": 1477, "23": 1585, "24": 1693, "25": 1801, "26": 1909, "27": 2018, "28": 2126, "29": 2234, "30": 2342, "31": 2450, "32": 2558, "33": 3390},
        "attribute_scaling_tiers": {"Vitality": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Switch to Virtuose Stance on breaking any Shield.",
                "tags": ["Trigger:OnShieldBreak", "Effect:StanceSwitch", "Stance:Virtuose"]
            },
            "lvl_10": {
                "description": "Free Aim shots break 2 shields.",
                "tags": ["Trigger:OnFreeAimShot", "Effect:BreakShields", "Value:2"]
            },
            "lvl_20": {
                "description": "In Virtuose Stance, all damage pierce Shields.",
                "tags": ["Condition:InVirtuoseStance", "Effect:PierceShields"]
            }
        },
        "acquisition_info": "Gestral Village (Eesda merchant purchase after duel)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "max_level": 33
    },
    {
        "name": "Stalum",
        "element": "Fire",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3228,
        "attributes": ["Luck", "Defense"],
        "power_by_level": {"1": 45, "2": 68, "3": 91, "4": 121, "5": 166, "6": 211, "7": 256, "8": 301, "9": 346, "10": 419, "11": 489, "12": 559, "13": 629, "14": 699, "15": 769, "16": 839, "17": 909, "18": 979, "19": 1049, "20": 1200, "21": 1303, "22": 1406, "23": 1509, "24": 1612, "25": 1715, "26": 1818, "27": 1921, "28": 2024, "29": 2127, "30": 2230, "31": 2333, "32": 2436, "33": 3228},
        "attribute_scaling_tiers": {"Luck": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Apply Burn on self on turn start. 10% increased damage for each self Burn stack.",
                "tags": ["Trigger:TurnStart", "Effect:ApplyBurnToSelf", "Stacks:1", "Effect:DamageBoost", "Condition:PerSelfBurnStack", "Value:0.1"]
            },
            "lvl_10": {
                "description": "Base Attack applies 2 Burn.",
                "tags": ["Trigger:OnBaseAttack", "Effect:AppliesStatus", "Status:Burn", "Stacks:2"]
            },
            "lvl_20": {
                "description": "While in Defensive Stance, receive Heal instead of Burn damage.",
                "tags": ["Condition:InDefensiveStance", "Effect:ConvertBurnDamageToHeal"]
            }
        },
        "acquisition_info": "The Continent (Enemy drop) n Hearts (Enemy drop)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Fire": "Increased damage for each self Burn stack"},
        "max_level": 33
    },
    {
        "name": "Tissenum",
        "element": "Earth",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3874,
        "attributes": ["Vitality", "Agility"],
        "power_by_level": {"1": 54, "2": 82, "3": 110, "4": 146, "5": 200, "6": 254, "7": 308, "8": 362, "9": 416, "10": 503, "11": 587, "12": 671, "13": 755, "14": 839, "15": 923, "16": 1007, "17": 1091, "18": 1175, "19": 1259, "20": 1440, "21": 1564, "22": 1688, "23": 1811, "24": 1935, "25": 2058, "26": 2182, "27": 2306, "28": 2429, "29": 2553, "30": 2676, "31": 2800, "32": 2924, "33": 3874},
        "attribute_scaling_tiers": {"Vitality": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Agility": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "In Defensive Stance, double Break damage.",
                "tags": ["Condition:InDefensiveStance", "Effect:DamageBoost", "DamageType:Break", "Value:2.0"]
            },
            "lvl_10": {
                "description": "Gain 9 AP on Breaking an enemy.",
                "tags": ["Trigger:OnBreakEnemy", "Effect:APGain", "Value:9"]
            },
            "lvl_20": {
                "description": "Breaking an enemy deals 3 high amount of Earth damage.",
                "tags": ["Trigger:OnBreakEnemy", "Effect:DealDamage", "DamageType:Earth", "Value:High", "Hits:3"]
            }
        },
        "acquisition_info": "Sirene (Tisseur drop)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {"Earth": "Double Break damage"},
        "max_level": 33
    },
    {
        "name": "Veremum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3293,
        "attributes": ["Luck", "Vitality"],
        "power_by_level": {"1": 46, "2": 70, "3": 93, "4": 124, "5": 170, "6": 216, "7": 262, "8": 308, "9": 353, "10": 428, "11": 499, "12": 571, "13": 642, "14": 713, "15": 785, "16": 856, "17": 928, "18": 999, "19": 1070, "20": 1224, "21": 1330, "22": 1435, "23": 1540, "24": 1645, "25": 1750, "26": 1855, "27": 1960, "28": 2065, "29": 2170, "30": 2275, "31": 2380, "32": 2485, "33": 3293},
        "attribute_scaling_tiers": {"Luck": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Vitality": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "If Stanceless, Base Attack switches to Offensive Stance.",
                "tags": ["Condition:Stanceless", "Effect:StanceSwitch", "Stance:Offensive"]
            },
            "lvl_10": {
                "description": "Counterattacks apply Defenceless.",
                "tags": ["Trigger:OnCounterattack", "Effect:AppliesStatus", "Status:Defenceless"]
            },
            "lvl_20": {
                "description": "+50% Critical Chance while in Offensive Stance.",
                "tags": ["Condition:InOffensiveStance", "Effect:StatBoost", "Stat:CritChance", "Value:0.5", "Operator:Add"]
            }
        },
        "acquisition_info": "Inside the Monolith (Mistra drop)",
        "stance_synergy": ["Offensive"],
        "element_interactions": {},
        "max_level": 33
    },
    {
        "name": "Volesterum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3293,
        "attributes": ["Vitality", "Agility"],
        "power_by_level": {"1": 46, "2": 70, "3": 93, "4": 124, "5": 170, "6": 216, "7": 262, "8": 308, "9": 353, "10": 428, "11": 499, "12": 571, "13": 642, "14": 713, "15": 785, "16": 856, "17": 928, "18": 999, "19": 1070, "20": 1224, "21": 1330, "22": 1435, "23": 1540, "24": 1645, "25": 1750, "26": 1855, "27": 1960, "28": 2065, "29": 2170, "30": 2275, "31": 2380, "32": 2485, "33": 3293},
        "attribute_scaling_tiers": {"Vitality": {"1": "D", "4": "C", "20": "B", "33": "A"}, "Agility": {"1": "C", "4": "B", "20": "A", "33": "S"}},
        "passive_effects": {
            "lvl_4": {
                "description": "+1 AP on Stance switch.",
                "tags": ["Trigger:OnStanceSwitch", "Effect:APGain", "Value:1"]
            },
            "lvl_10": {
                "description": "If Stanceless, Base Attack switches to Defensive Stance.",
                "tags": ["Condition:Stanceless", "Effect:StanceSwitch", "Stance:Defensive"]
            },
            "lvl_20": {
                "description": "Recover 5% Health on Stance switch.",
                "tags": ["Trigger:OnStanceSwitch", "Effect:SelfHeal", "Value:0.05"]
            }
        },
        "acquisition_info": "Lumiere (Act 3, Cribappa merchant purchase)",
        "stance_synergy": ["Defensive"],
        "element_interactions": {},
        "max_level": 33
    },
    {
        "name": "Yeverum",
        "element": "Physical",
        "weapon_type": "Weapon_Rapier",
        "spoiler_info_json": {"act_available": 1},
        "power at max level": 3358,
        "attributes": ["Defense", "Agility"],
        "power_by_level": {"1": 47, "2": 71, "3": 95, "4": 126, "5": 173, "6": 220, "7": 267, "8": 314, "9": 360, "10": 436, "11": 509, "12": 582, "13": 655, "14": 727, "15": 800, "16": 873, "17": 946, "18": 1019, "19": 1091, "20": 1248, "21": 1356, "22": 1463, "23": 1570, "24": 1677, "25": 1784, "26": 1891, "27": 1998, "28": 2105, "29": 2213, "30": 2320, "31": 2427, "32": 2534, "33": 3358},
        "attribute_scaling_tiers": {"Defense": {"1": "C", "4": "B", "20": "A", "33": "S"}, "Agility": {"1": "D", "4": "C", "20": "B", "33": "A"}},
        "passive_effects": {
            "lvl_4": {
                "description": "Applying Shell also applies 1 Shield.",
                "tags": ["Trigger:OnApplyShell", "Effect:ApplyShield", "Value:1"]
            },
            "lvl_10": {
                "description": "On applying Shields, also give 1 AP.",
                "tags": ["Trigger:OnApplyShield", "Effect:APGain", "Value:1"]
            },
            "lvl_20": {
                "description": "On switching to Virtuose Stance, double all Shields on allies.",
                "tags": ["Trigger:OnStanceSwitch", "Condition:ToVirtuoseStance", "Effect:DoubleShieldsOnAllies"]
            }
        },
        "acquisition_info": "Renoir's Drafts (Grour merchant purchase after duel)",
        "stance_synergy": ["Virtuose"],
        "element_interactions": {},
        "max_level": 33
    }
]
