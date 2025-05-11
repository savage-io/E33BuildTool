# app/game_data_definitions/maelle_skills.py

MAELLE_SKILL_DEFINITIONS = [
    {
        "name": "Offensive Switch",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 1},
        "ap_cost": 1,
        "description": "Low (weapon's element) damage. Applies Defenceless. 1 hit.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "Low", "hits": 1, 
                         "status_applied_to_target": [{"name": "Defenceless", "duration_turns": 3, "application_timing": "on_skill_completion"}]},
        "mechanics_json": {"stance_entry": "Offensive Stance", "unlock_method": "Starting Skill"},
        "tags_json": ["Damage:WeaponElement", "AppliesStatus:Defenceless", "Stance:Offensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/offensive_switch.png"
    },
    {
        "name": "Last Chance",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 1,
        "description": "Reduces self-Health to 1 but refills all AP.",
        "effects_json": {"self_hp_to": 1, "ap_refill": "all"},
        "mechanics_json": {"stance_switch": "Virtuose Stance", "prerequisite_skill": "Mezzo Forte"},
        "tags_json": ["Mechanic:APRefill", "Mechanic:SelfHPReduction", "Stance:Virtuose:Switch", "Role:Utility", "Mechanic:Emergency"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/last_chance.png"
    },
    {
        "name": "Virtuose Strike", # Gradient Attack
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 0, 
        "description": "High Physical damage. 5 hits.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "High", "hits": 5, "gradient_charge_cost": 1},
        "mechanics_json": {"unlock_method": "Automatic Gradient Unlock"},
        "tags_json": ["Damage:Physical", "Mechanic:GradientAttack", "Role:DPS", "Target:Single"],
        "is_gradient_attack": True,
        "icon_url": "/static/images/skills/virtuose_strike.png"
    },
    {
        "name": "Mezzo Forte",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 1,
        "description": "Reapplies current stance and gives 2-4 AP.",
        "effects_json": {"ap_gain_range": [2, 4]},
        "mechanics_json": {"stance_interaction": "Maintains current stance", "prerequisite_skill": "Degagement"},
        "tags_json": ["Mechanic:APGeneration", "Stance:MaintainCurrent", "Role:Support", "Role:Utility"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/mezzo_forte.png"
    },
    {
        "name": "Degagement",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 2,
        "description": "Low Fire damage. 1 hit. Target becomes weak to Fire damage for 2 turns.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Low", "hits": 1, 
                         "status_applied_to_target": [{"name": "WeakToFire", "duration_turns": 2, "application_timing": "on_skill_completion"}]},
        "mechanics_json": {"stance_entry": "Offensive Stance", "prerequisite_skill": "Spark or Guard Down"}, # Representing "OR" condition
        "tags_json": ["Damage:Fire", "AppliesStatus:WeakToFire", "Stance:Offensive:Entry", "Role:DPS", "Role:Debuffer", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/degagement.png"
    },
    {
        "name": "Phoenix Flame", # Gradient Attack
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 0,
        "description": "Applies 10 Burn to all enemies and revives all allies with 50 to 70% Health.",
        "effects_json": {"target_type": "all_enemies", "status_applied_to_target": [{"name": "Burn", "stacks": 10, "application_timing": "on_skill_completion"}], 
                         "effect_on_allies": {"type": "revive", "hp_percent_range": [50, 70]}, "gradient_charge_cost": 2},
        "mechanics_json": {"unlock_method": "Relationship Level 4 Unlock"},
        "tags_json": ["AppliesStatus:Burn", "Mechanic:Revive", "Target:AllEnemies", "Target:AllAllies", "Mechanic:GradientAttack", "Role:Support", "Role:DPS"],
        "is_gradient_attack": True,
        "icon_url": "/static/images/skills/phoenix_flame.png"
    },
    {
        "name": "Spark",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 3,
        "description": "Low Fire damage. 1 hit. Applies 3 Burn. Offensive Stance: Applies 2 more Burn.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Low", "hits": 1, 
                         "status_applied_to_target": [{"name": "Burn", "stacks": 3, "application_timing": "on_skill_completion"}]},
        "mechanics_json": {"stance_entry": "Defensive Stance", 
                           "conditional_effect": {"condition": "in_offensive_stance", "effect": {"status_applied_to_target_additive": [{"name": "Burn", "stacks": 2, "application_timing": "on_skill_completion"}]}},
                           "prerequisite_skill": "Offensive Switch"},
        "tags_json": ["Damage:Fire", "AppliesStatus:Burn", "Stance:Defensive:Entry", "Synergy:OffensiveStance", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/spark.png"
    },
    {
        "name": "Breaking Rules",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 3,
        "description": "Low Physical damage. 2 hits. Destroys all target's Shields. Gains 1 AP per Shield destroyed. If target is Defenceless, play a second turn.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "Low", "hits": 2, "shield_destroy": "all", "ap_gain_per_shield": 1},
        "mechanics_json": {"stance_entry": "Offensive Stance", 
                           "conditional_effect": {"condition": "target_is_defenceless", "effect": "extra_turn"},
                           "prerequisite_skill": "Fleuret Fury"},
        "tags_json": ["Damage:Physical", "Mechanic:ShieldBreak", "Mechanic:APGeneration", "Synergy:DefencelessTarget", "Mechanic:ExtraTurn", "Stance:Offensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/breaking_rules.png"
    },
    {
        "name": "Swift Stride",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 3,
        "description": "Low Physical damage. 1 hit. Switches to Virtuose Stance if target is Burning. Regains 0-2 AP.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "Low", "hits": 1, "ap_gain_range": [0, 2]},
        "mechanics_json": {"conditional_stance_switch": {"condition": "target_is_burning", "stance": "Virtuose Stance"},
                           "prerequisite_skill": "Percée"}, # Corrected from Percee in your list
        "tags_json": ["Damage:Physical", "Stance:Virtuose:ConditionalSwitch", "Synergy:BurningTarget", "Mechanic:APGeneration", "Role:Utility", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/swift_stride.png"
    },
    {
        "name": "Égide",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 3,
        "description": "Protects allies by taking damage in their place for 2 turns. Duration extended by 1 on gaining Shell. (Single-target hits only).",
        "effects_json": {"effect_type": "protect_allies_take_damage", "duration_turns": 2, "duration_extension_on_shell_gain": 1, "target_scope": "single_target_hits_on_allies"},
        "mechanics_json": {"stance_entry": "Defensive Stance", "prerequisite_skill": "Guard Up"},
        "tags_json": ["Mechanic:ProtectAllies", "Mechanic:Taunt", "Synergy:Shell", "Stance:Defensive:Entry", "Role:Tank", "Role:Support"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/egide.png"
    },
    {
        "name": "Guard Up",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 3,
        "description": "Applies Shell to up to 3 allies for 3 turns. Regains 0-2 AP.", # Added AP regain from skill table
        "effects_json": {"status_applied_to_allies": [{"name": "Shell", "duration_turns": 3}], "max_allies_targeted": 3, "ap_gain_range": [0,2]},
        "mechanics_json": {"stance_entry": "Defensive Stance", "prerequisite_skill": "Swift Stride"},
        "tags_json": ["AppliesStatus:Shell", "Target:Allies", "Stance:Defensive:Entry", "Role:Support", "Mechanic:APGeneration"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/guard_up.png"
    },
    {
        "name": "Guard Down",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 3,
        "description": "Applies Defenceless to all enemies for 3 turns.",
        "effects_json": {"target_type": "all_enemies", "status_applied_to_target": [{"name": "Defenceless", "duration_turns": 3, "application_timing": "on_skill_completion"}]},
        "mechanics_json": {"stance_entry": "Offensive Stance", "prerequisite_skill": "Guard Up or Degagement"},
        "tags_json": ["AppliesStatus:Defenceless", "Target:AllEnemies", "Stance:Offensive:Entry", "Role:Debuffer", "Role:Support"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/guard_down.png"
    },
    {
        "name": "Gommage", # Gradient Attack
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 0,
        "description": "Kills weak targets. Otherwise deals extreme Void damage. 1 hit.",
        "effects_json": {"conditional_effect": {"condition": "target_is_weak", "effect": "instant_kill"}, 
                         "alternative_effect": {"damage_type": "Void", "damage_scale": "Extreme", "hits": 1}, "gradient_charge_cost": 3},
        "mechanics_json": {"unlock_method": "Relationship Level 7 Unlock"},
        "tags_json": ["Damage:Void", "Mechanic:InstantKill", "Mechanic:GradientAttack", "Role:DPS", "Target:Single"],
        "is_gradient_attack": True,
        "icon_url": "/static/images/skills/gommage.png"
    },
    {
        "name": "Combustion",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 4,
        "description": "Deals medium single target Physical Damage (2 Hits). Consumes up to 10 Burn for increased damage.", # Clarified target
        "effects_json": {"damage_type": "Physical", "damage_scale": "Medium", "hits": 2, "target_type": "single",
                         "consumes_status_for_buff": {"status_name": "Burn", "max_stacks_consumed": 10, "effect": "increased_damage"}},
        "mechanics_json": {"stance_entry": "Offensive Stance", "prerequisite_skill": "Rain of Fire"},
        "tags_json": ["Damage:Physical", "Mechanic:ConsumeBurn", "Synergy:BurnTarget", "Stance:Offensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/combustion.png"
    },
    {
        "name": "Fencer's Flurry",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 4,
        "description": "Deals medium damage to all enemies (1 hit) using weapon's element. Applies Defenceless for 1 turn.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "Medium", "target_type": "all_enemies", "hits": 1, 
                         "status_applied_to_target": [{"name": "Defenceless", "duration_turns": 1, "application_timing": "on_skill_completion"}]},
        "mechanics_json": {"stance_entry": "Offensive Stance", "prerequisite_skill": "Breaking Rules"},
        "tags_json": ["Damage:WeaponElement", "AppliesStatus:Defenceless", "Target:AllEnemies", "Stance:Offensive:Entry", "Role:DPS", "Role:Debuffer"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/fencers_flurry.png"
    },
    {
        "name": "Rain of Fire",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 5,
        "description": "Deals medium single target Fire damage (2 hits). Applies 3 Burn per hit. Defensive Stance: Applies 2 more Burn per hit.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Medium", "target_type": "single", "hits": 2, 
                         "status_applied_to_target_per_hit": [{"name": "Burn", "stacks": 3}]},
        "mechanics_json": {"stance_entry": "Offensive Stance",  # "Enters Offensive Stance (Implied)" from PDF skill table
                           "conditional_effect": {"condition": "in_defensive_stance", "effect": {"status_applied_to_target_additive_per_hit": [{"name": "Burn", "stacks": 2}]}},
                           "prerequisite_skill": "Degagement"},
        "tags_json": ["Damage:Fire", "AppliesStatus:Burn", "Stance:Offensive:Entry", "Synergy:DefensiveStance", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/rain_of_fire.png"
    },
    {
        "name": "Revenge",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 5,
        "description": "Deals high single target Fire damage (1 hit). Damage increased for each hit received since the previous turn. Can Break.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "High", "target_type": "single", "hits": 1, "can_break": True, 
                         "dynamic_damage_increase": {"condition": "per_hit_received_since_last_turn"}},
        "mechanics_json": {"stance_entry": "Offensive Stance", "prerequisite_skill": "Combustion"},
        "tags_json": ["Damage:Fire", "Mechanic:Break", "Mechanic:DamageScaling", "Stance:Offensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/revenge.png"
    },
    {
        "name": "Percée", # Percee
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 5,
        "description": "Deals medium single target Physical damage (1 hit). Increased damage to Marked targets. Offensive Stance: Increased damage. Virtuose Stance: Costs 2 AP.", # Integrated info
        "effects_json": {"damage_type": "Physical", "damage_scale": "Medium", "target_type": "single", "hits": 1, "bonus_vs_marked": True},
        "mechanics_json": {"stance_entry": "Defensive Stance", 
                           "conditional_effect": [ # List for multiple distinct conditional effects
                               {"condition": "in_offensive_stance", "effect_description": "Increased damage"}, # How to quantify "increased damage"? Tag for now.
                               {"condition": "in_virtuose_stance", "effect": {"new_ap_cost": 2}}
                           ],
                           "unlock_method": "Starting Skill"},
        "tags_json": ["Damage:Physical", "Synergy:MarkedTarget", "Stance:Defensive:Entry", "Synergy:OffensiveStance", "Synergy:VirtuoseStance", "Mechanic:APCostChange", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/percee.png"
    },
    {
        "name": "Burning Canvas",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 5,
        "description": "High single target Void damage. 5 hits. Applies 1 Burn per hit. Damage increased for each Burn on the target.",
        "effects_json": {"damage_type": "Void", "damage_scale": "High", "target_type": "single", "hits": 5, 
                         "status_applied_to_target_per_hit": [{"name": "Burn", "stacks": 1}], 
                         "dynamic_damage_increase": {"condition": "per_burn_on_target"}},
        "mechanics_json": {"stance_entry": "Offensive Stance", "prerequisite_skill": "Phantom Strike or Stendhal"},
        "tags_json": ["Damage:Void", "AppliesStatus:Burn", "Mechanic:DamageScaling", "Synergy:BurnTarget", "Stance:Offensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/burning_canvas.png"
    },
    {
        "name": "Fleuret Fury",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 6,
        "description": "Deals high single target Physical damage (3 hits). Can Break. If used in Virtuose Stance, stay in Virtuose Stance. Enters Defensive Stance otherwise.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "High", "target_type": "single", "hits": 3, "can_break": True},
        "mechanics_json": {"conditional_stance_interaction": {"condition": "in_virtuose_stance", "effect_on_stance": "stay_in_virtuose_stance"}, 
                           "default_stance_entry": "Defensive Stance", # Changed from "Defensive Stance (Implied)"
                           "prerequisite_skill": "Guard Up"},
        "tags_json": ["Damage:Physical", "Mechanic:Break", "Stance:Virtuose:Maintain", "Stance:Defensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/fleuret_fury.png"
    },
    {
        "name": "Momentum Strike",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 7,
        "description": "Deals high single target damage (1 hit) using weapon's element. Increased damage to Marked targets. Cost reduced to 4 AP if used in Virtuose Stance. Enters Defensive Stance.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "High", "target_type": "single", "hits": 1, "bonus_vs_marked": True},
        "mechanics_json": {"stance_entry": "Defensive Stance", 
                           "conditional_effect": {"condition": "in_virtuose_stance", "effect": {"new_ap_cost": 4}},
                           "prerequisite_skill": "Égide"},
        "tags_json": ["Damage:WeaponElement", "Synergy:MarkedTarget", "Stance:Defensive:Entry", "Synergy:VirtuoseStance", "Mechanic:APCostChange", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/momentum_strike.png"
    },
    {
        "name": "Phantom Strike",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 7,
        "description": "Deals very high Void damage to all enemies (4 hits). Also gives +35% of a Gradient Charge.",
        "effects_json": {"damage_type": "Void", "damage_scale": "Very High", "target_type": "all_enemies", "hits": 4, "gradient_charge_gain_percent": 35},
        "mechanics_json": {"stance_entry": "Defensive Stance", "prerequisite_skill": "Offensive Switch or Burning Canvas"},
        "tags_json": ["Damage:Void", "Target:AllEnemies", "Mechanic:GradientChargeGain", "Stance:Defensive:Entry", "Role:DPS"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/phantom_strike.png"
    },
    {
        "name": "Gustave's Homage", # Story Unlock / Potential Spoiler/Hidden
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 8,
        "description": "Deals high single target Lightning damage (8 hits). Increased damage to Marked targets, Doesn't remove Mark.",
        "effects_json": {"damage_type": "Lightning", "damage_scale": "High", "target_type": "single", "hits": 8, "bonus_vs_marked": True, "does_not_remove_mark": True},
        "mechanics_json": {"unlock_method": "Story Unlock (After Forgotten Battlefield)", "stance_interaction": "Not specified"},
        "tags_json": ["Damage:Lightning", "Synergy:MarkedTarget", "Mechanic:PreserveMark", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/gustaves_homage.png"
    },
    {
        "name": "Stendhal",
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 8,
        "description": "Deals extreme single target Void damage (1 hit). Removes self-Shields and self applies Defenceless.",
        "effects_json": {"damage_type": "Void", "damage_scale": "Extreme", "target_type": "single", "hits": 1, 
                         "self_removes_shields": True, "status_applied_to_self": [{"name": "Defenceless", "application_timing": "on_skill_completion"}]},
        "mechanics_json": {"stance_entry": "Stanceless", "prerequisite_skill": "Percée or Burning Canvas"},
        "tags_json": ["Damage:Void", "Mechanic:SelfDebuff", "AppliesStatus:SelfDefenceless", "Stance:Stanceless:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/stendhal.png"
    },
    {
        "name": "Payback", # Potential Spoiler/Hidden
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 9,
        "description": "Deals very high single target Physical damage (1 hit). Reduced AP cost for each attack parried since last turn. Can Break.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "Very High", "target_type": "single", "hits": 1, "can_break": True},
        "mechanics_json": {"ap_cost_reduction_condition": "per_attack_parried_since_last_turn", 
                           "stance_entry": "Offensive Stance", # From PDF skill table
                           "prerequisite_skill": "Last Chance or Momentum Strike"}, # Last Chance in PDF, Momentum Strike from your list
        "tags_json": ["Damage:Physical", "Mechanic:Break", "Mechanic:APCostReduction", "Synergy:Parry", "Stance:Offensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/payback.png"
    },
    {
        "name": "Sword Ballet", # Potential Spoiler/Hidden
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 9,
        "description": "Deals extreme single target damage (5 hits) using weapon's element. Critical Hits deal double damage.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "Extreme", "target_type": "single", "hits": 5, "critical_hit_bonus_multiplier": 2.0}, # Assuming 2.0 means total crit damage x2
        "mechanics_json": {"stance_entry": "Defensive Stance", "prerequisite_skill": "Fencer's Flurry"},
        "tags_json": ["Damage:WeaponElement", "Mechanic:CritDamageBonus", "Stance:Defensive:Entry", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/sword_ballet.png"
    },
    {
        "name": "Pyrolyse", # Potential Spoiler/Hidden
        "character_name": "Maelle",
        "spoiler_info_json": {"act_available": 2},
        "ap_cost": 9,
        "description": "Deals extreme single target Fire damage (3 hits). Applies 5 Burn per hit. Offensive Stance: Applies 2 more Burn per hit.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Extreme", "target_type": "single", "hits": 3, 
                         "status_applied_to_target_per_hit": [{"name": "Burn", "stacks": 5}]},
        "mechanics_json": {"stance_entry": "Offensive Stance", # From PDF skill table
                           "conditional_effect": {"condition": "in_offensive_stance", "effect": {"status_applied_to_target_additive_per_hit": [{"name": "Burn", "stacks": 2}]}},
                           "prerequisite_skill": "Revenge"},
        "tags_json": ["Damage:Fire", "AppliesStatus:Burn", "Stance:Offensive:Entry", "Synergy:OffensiveStance", "Role:DPS", "Target:Single"],
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/pyrolyse.png"
    }
]
# Notes on structuring effects_json and mechanics_json:
# - Be consistent with keys.
# - "damage_scale": "Low", "Medium", "High", "Very High", "Extreme"
# - "status_applied": [{"name": "Defenceless", "duration_turns": 3, "stacks": 1 (default if not specified)}]
# - "conditional_effect": {"condition": "target_is_burning", "effect": { ... another effects_json like structure ... }}
# - "stance_entry": Name of the stance entered, or "Maintains current stance", or "Switches to X if Y"
# - This detailed structuring is for your recommendation engine later.
# - The plain text `description` is good for direct display.
# - I've taken some liberties interpreting the short descriptions into structured data and integrated info from your previous document. You'll need to review for accuracy.
# - Icon URLs are placeholders.
