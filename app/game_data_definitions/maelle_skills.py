# Maelle's skill data# app/game_data_definitions/maelle_skills.py

MAELLE_SKILL_DEFINITIONS = [
    {
        "name": "Offensive Switch",
        "character_name": "Maelle",
        "ap_cost": 1,
        "description": "Low (weapon's element) damage. Applies Defenceless. 1 hit.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "Low", "hits": 1, "status_applied": [{"name": "Defenceless", "duration_turns": 3}]}, # Assuming duration
        "mechanics_json": {"stance_entry": "Offensive Stance"}, # From previous doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/offensive_switch.png"
    },
    {
        "name": "Last Chance",
        "character_name": "Maelle",
        "ap_cost": 1,
        "description": "Reduces self-Health to 1 but refills all AP.",
        "effects_json": {"self_hp_to": 1, "ap_refill": "all"},
        "mechanics_json": {"stance_switch": "Virtuose Stance"},
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/last_chance.png"
    },
    {
        "name": "Virtuose Strike", # This is a Gradient Attack based on previous doc
        "character_name": "Maelle",
        "ap_cost": 0, # Gradient attacks usually use charges, not AP directly
        "description": "High Physical damage. 5 hits.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "High", "hits": 5, "gradient_charge_cost": 1},
        "mechanics_json": {"unlock_method": "Automatic Gradient Unlock"}, # From previous doc
        "is_gradient_attack": True, # MARKED AS GRADIENT
        "icon_url": "/static/images/skills/virtuose_strike.png"
    },
    {
        "name": "Mezzo Forte",
        "character_name": "Maelle",
        "ap_cost": 1,
        "description": "Reapplies current stance and gives 2-4 AP.",
        "effects_json": {"ap_gain_range": [2, 4]},
        "mechanics_json": {"stance_interaction": "Maintains current stance"}, # From previous doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/mezzo_forte.png"
    },
    {
        "name": "Degagement",
        "character_name": "Maelle",
        "ap_cost": 2,
        "description": "Low Fire damage. 1 hit. Target becomes weak to Fire damage for 2 turns.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Low", "hits": 1, "status_applied_target": [{"name": "WeakToFire", "duration_turns": 2}]},
        "mechanics_json": {"stance_entry": "Offensive Stance"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/degagement.png"
    },
    {
        "name": "Phoenix Flame", # This is a Gradient Attack
        "character_name": "Maelle",
        "ap_cost": 0, 
        "description": "Applies 10 Burn to all enemies and revives all allies with 50 to 70% Health.",
        "effects_json": {"target_type": "all_enemies", "status_applied": [{"name": "Burn", "stacks": 10}], "allies_revive_hp_percent_range": [50, 70], "gradient_charge_cost": 2},
        "mechanics_json": {"unlock_method": "Relationship Level 4 Unlock"}, # From prev doc
        "is_gradient_attack": True, # MARKED AS GRADIENT
        "icon_url": "/static/images/skills/phoenix_flame.png"
    },
    {
        "name": "Spark",
        "character_name": "Maelle",
        "ap_cost": 3,
        "description": "Low Fire damage. 1 hit. Applies 3 Burn. Offensive Stance: Applies 2 more Burn.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Low", "hits": 1, "status_applied": [{"name": "Burn", "stacks": 3}]},
        "mechanics_json": {"stance_entry": "Defensive Stance", "conditional_effect": {"condition": "in_offensive_stance", "effect": {"status_applied_additive": [{"name": "Burn", "stacks": 2}]}}}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/spark.png"
    },
    {
        "name": "Breaking Rules",
        "character_name": "Maelle",
        "ap_cost": 3,
        "description": "Low Physical damage. 2 hits. Destroys Shields and gains 1 AP per Shield. If target is Defenceless, play a second turn.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "Low", "hits": 2, "shield_destroy": True, "ap_gain_per_shield": 1},
        "mechanics_json": {"stance_entry": "Offensive Stance", "conditional_effect": {"condition": "target_is_defenceless", "effect": "extra_turn"}}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/breaking_rules.png"
    },
    {
        "name": "Swift Stride",
        "character_name": "Maelle",
        "ap_cost": 3,
        "description": "Low Physical damage. 1 hit. Switches to Virtuose Stance if target is Burning. Regains 0-2 AP.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "Low", "hits": 1, "ap_gain_range": [0, 2]},
        "mechanics_json": {"conditional_stance_switch": {"condition": "target_is_burning", "stance": "Virtuose Stance"}},
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/swift_stride.png"
    },
    {
        "name": "Égide", # Egide
        "character_name": "Maelle",
        "ap_cost": 3,
        "description": "Protects allies by taking damage in their place for 2 turns. Duration is extended by 1 on gaining Shell.",
        "effects_json": {"effect_type": "protect_allies", "duration_turns": 2, "duration_extension_on_shell_gain": 1, "target_scope": "single_target_hits_on_allies"},
        "mechanics_json": {"stance_entry": "Defensive Stance (Implied)"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/egide.png"
    },
    {
        "name": "Guard Up",
        "character_name": "Maelle",
        "ap_cost": 3,
        "description": "Applies Shell, reducing damage taken, to up to 3 allies for 3 turns.",
        "effects_json": {"status_applied_allies": [{"name": "Shell", "duration_turns": 3}], "max_allies_targeted": 3},
        "mechanics_json": {"stance_entry": "Defensive Stance (Implied)"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/guard_up.png"
    },
    {
        "name": "Guard Down",
        "character_name": "Maelle",
        "ap_cost": 3,
        "description": "Applies Defenceless to all enemies.",
        "effects_json": {"target_type": "all_enemies", "status_applied": [{"name": "Defenceless", "duration_turns": 3}]}, # Assuming 3 turns
        "mechanics_json": {"stance_entry": "Offensive Stance"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/guard_down.png"
    },
    {
        "name": "Gommage", # This is a Gradient Attack
        "character_name": "Maelle",
        "ap_cost": 0,
        "description": "Kills weak targets. Otherwise deals extreme Void damage. 1 hit.",
        "effects_json": {"conditional_effect": {"condition": "target_is_weak", "effect": "instant_kill"}, "alternative_effect": {"damage_type": "Void", "damage_scale": "Extreme", "hits": 1}, "gradient_charge_cost": 3},
        "mechanics_json": {"unlock_method": "Relationship Level 7 Unlock"}, # From prev doc
        "is_gradient_attack": True, # MARKED AS GRADIENT
        "icon_url": "/static/images/skills/gommage.png"
    },
    {
        "name": "Combustion",
        "character_name": "Maelle",
        "ap_cost": 4,
        "description": "Medium Physical damage. 2 hits. Consumes up to 10 Burn for increased damage.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "Medium", "hits": 2, "consumes_status_for_buff": {"status_name": "Burn", "max_stacks_consumed": 10, "effect": "increased_damage"}},
        "mechanics_json": {"stance_entry": "Offensive Stance (Implied)"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/combustion.png"
    },
    {
        "name": "Fencer's Flurry",
        "character_name": "Maelle",
        "ap_cost": 4,
        "description": "Medium (weapon's element) damage to all enemies. 1 hit. Applies Defenceless for 1 turn.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "Medium", "target_type": "all_enemies", "hits": 1, "status_applied": [{"name": "Defenceless", "duration_turns": 1}]},
        "mechanics_json": {"stance_entry": "Offensive Stance (Implied)"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/fencers_flurry.png"
    },
    {
        "name": "Rain of Fire",
        "character_name": "Maelle",
        "ap_cost": 5,
        "description": "Medium Fire damage and applies 3 Burn per hit. 2 hits. Defensive Stance: applies 2 more Burn per hit.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Medium", "hits": 2, "status_applied_per_hit": [{"name": "Burn", "stacks": 3}]},
        "mechanics_json": {"stance_entry": "Offensive Stance (Implied)", "conditional_effect": {"condition": "in_defensive_stance", "effect": {"status_applied_additive_per_hit": [{"name": "Burn", "stacks": 2}]}}}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/rain_of_fire.png"
    },
    {
        "name": "Revenge",
        "character_name": "Maelle",
        "ap_cost": 5,
        "description": "High Fire damage. 1 hit. Damage increased for each hit received this turn. Can Break.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "High", "hits": 1, "can_break": True, "damage_increase_condition": "per_hit_received_this_turn"},
        "mechanics_json": {"stance_entry": "Offensive Stance (Implied)"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/revenge.png"
    },
    {
        "name": "Percée", # Percee
        "character_name": "Maelle",
        "ap_cost": 5,
        "description": "Low Physical damage. 1 hit. Offensive Stance: Increased damage. Virtuose Stance: Costs 2 AP.", # Description from list slightly different from prev doc, integrating
        "effects_json": {"damage_type": "Physical", "damage_scale": "Low", "hits": 1},
        "mechanics_json": {"stance_entry": "Defensive Stance", "conditional_effect": [{"condition": "in_offensive_stance", "effect": "increased_damage"}, {"condition": "in_virtuose_stance", "effect": {"new_ap_cost": 2}}]}, # From prev doc / integrating
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/percee.png"
    },
    {
        "name": "Burning Canvas",
        "character_name": "Maelle",
        "ap_cost": 5,
        "description": "High single target Void damage. 5 hits. Applies 1 Burn per hit. Damage increased for each Burn on the target.",
        "effects_json": {"damage_type": "Void", "damage_scale": "High", "hits": 5, "status_applied_per_hit": [{"name": "Burn", "stacks": 1}], "damage_increase_condition": "per_burn_on_target"},
        "mechanics_json": {"stance_entry": "Offensive Stance"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/burning_canvas.png"
    },
    {
        "name": "Fleuret Fury",
        "character_name": "Maelle",
        "ap_cost": 6,
        "description": "High Physical damage. 3 hits. If in Virtuose Stance, stay in Virtuose Stance. Can Break.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "High", "hits": 3, "can_break": True},
        "mechanics_json": {"conditional_stance_interaction": {"condition": "in_virtuose_stance", "effect": "stay_in_virtuose_stance"}, "default_stance_entry": "Defensive Stance (Implied)"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/fleuret_fury.png"
    },
    {
        "name": "Momentum Strike",
        "character_name": "Maelle",
        "ap_cost": 7,
        "description": "High (weapon's element) damage. 1 hit. Increased damage to Marked targets. Virtuose Stance: Costs 4 AP.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "High", "hits": 1, "bonus_vs_marked": True},
        "mechanics_json": {"stance_entry": "Defensive Stance (Implied)", "conditional_effect": {"condition": "in_virtuose_stance", "effect": {"new_ap_cost": 4}}}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/momentum_strike.png"
    },
    {
        "name": "Phantom Strike",
        "character_name": "Maelle",
        "ap_cost": 7,
        "description": "Very high Void damage to all enemies. 4 hits. Also gives +35% of a Gradient Charge.",
        "effects_json": {"damage_type": "Void", "damage_scale": "Very High", "target_type": "all_enemies", "hits": 4, "gradient_charge_gain_percent": 35},
        "mechanics_json": {"stance_entry": "Defensive Stance"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/phantom_strike.png"
    },
    {
        "name": "Gustave's Homage", # Story Unlock
        "character_name": "Maelle",
        "ap_cost": 8,
        "description": "High Lightning damage. 8 hits. Increased damage to Marked targets. Doesn't remove Mark.",
        "effects_json": {"damage_type": "Lightning", "damage_scale": "High", "hits": 8, "bonus_vs_marked": True, "does_not_remove_mark": True},
        "mechanics_json": {"unlock_method": "Story Unlock (After Forgotten Battlefield)", "stance_interaction": "Not specified"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/gustaves_homage.png"
    },
    {
        "name": "Stendhal",
        "character_name": "Maelle",
        "ap_cost": 8,
        "description": "Extreme Void damage. 1 hit. Removes self-Shields and self applies Defenceless.",
        "effects_json": {"damage_type": "Void", "damage_scale": "Extreme", "hits": 1, "self_removes_shields": True, "self_status_applied": [{"name": "Defenceless"}]},
        "mechanics_json": {"stance_entry": "Stanceless"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/stendhal.png"
    },
    {
        "name": "Payback",
        "character_name": "Maelle",
        "ap_cost": 9,
        "description": "Very high Physical damage. 1 hit. Reduced AP cost for each attack parried since last turn. Can Break.",
        "effects_json": {"damage_type": "Physical", "damage_scale": "Very High", "hits": 1, "can_break": True},
        "mechanics_json": {"ap_cost_reduction_condition": "per_attack_parried_since_last_turn", "stance_entry": "Offensive Stance (Implied)"}, # From prev doc
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/payback.png"
    },
    {
        "name": "Sword Ballet",
        "character_name": "Maelle",
        "ap_cost": 9,
        "description": "Extreme (weapon's element) damage. 5 hits. Critical Hits deal double damage.",
        "effects_json": {"damage_type": "weapon_element", "damage_scale": "Extreme", "hits": 5, "critical_hit_bonus": "double_damage"},
        "mechanics_json": {"stance_entry": "Defensive Stance (Implied)"}, # From prev doc, though "Enters Defensive" seems odd for a high cost attack. Double check.
        "is_gradient_attack": False,
        "icon_url": "/static/images/skills/sword_ballet.png"
    },
    {
        "name": "Pyrolyse",
        "character_name": "Maelle",
        "ap_cost": 9,
        "description": "Extreme Fire damage. 3 hits. Applies 5 Burn per hit. Offensive Stance: Applies 2 more Burn per hit.",
        "effects_json": {"damage_type": "Fire", "damage_scale": "Extreme", "hits": 3, "status_applied_per_hit": [{"name": "Burn", "stacks": 5}]},
        "mechanics_json": {"stance_entry": "Offensive Stance (Implied)", "conditional_effect": {"condition": "in_offensive_stance", "effect": {"status_applied_additive_per_hit": [{"name": "Burn", "stacks": 2}]}}}, # From prev doc
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
