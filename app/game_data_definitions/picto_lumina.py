PICTOS_LUMINAS_DEFINITIONS = [
{
    "name": "Accelerating Heal",
    "lumina_description": "Healing an ally also applies Rush for 1 turn.",
    "lumina_lp_cost": 5,
    "lumina_type": "Support",
    "lumina_effect_details_json": {
        "trigger": "on_healing_ally",
        "applies_status_to_healed_ally": [{"name": "Rush", "duration_turns": 1}]
    },
    "picto_variants_json": {
        "9": { # Key is the Picto Level from your sheet
            "stat_bonuses": {"Health": 329, "Speed": 65},
            "acquisition_info": "Acquisition for Lvl 9 Picto", # You'll fill this
            "icon_url": "/static/pictos/accelerating_heal_lvl9.png"
        }
        # If "Accelerating Heal" had another Picto version at a different level, add it here:
        # "15": {"stat_bonuses": {"Health": 600, "Speed": 100}, ... }
    },
    "tags_json": ["LuminaType:Support", "Trigger:OnHeal", "AppliesStatus:Rush", "Buff:Ally"],
    "spoiler_info_json": {"act_available": 1} # Based on lowest Picto level
},
{
    "name": "Accelerating Last Stand", 
    "lumina_description": "Gain Rush if fighting alone",
    "lumina_lp_cost": 3,
    "lumina_type": "Support",
    "lumina_effect_details_json": {
        "condition": "is_fighting_alone", # Tags: Condition:Solo, Condition:PartySize1, Condition:SelfOnlyAlive
        "applies_status_to_self": [{"name": "Rush"}] # TODO: Specify Rush duration if known, or add "duration_type": "conditional"
    },
    "picto_variants_json": {
        "6": { 
            "stat_bonuses": {"Health": 168, "Defense": 34},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/accelerating_last_stand_lvl6.png"
        }
    },
    "tags_json": ["PictoType:Support", "LuminaType:Support", "Condition:Solo", "AppliesStatus:Rush", "Buff:Self"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Accelerating Tint", 
    "lumina_description": "Healing Tints also apply Rush",
    "lumina_lp_cost": 5,
    "lumina_type": "Support",
    "lumina_effect_details_json": {
        "trigger": "on_using_healing_tint", # TODO: Confirm 'HealingTint' as a valid skill tag/category
        "applies_status_to_target_of_tint": [{"name": "Rush"}] # TODO: Specify Rush duration if known
    },
    "picto_variants_json": {
        "25": {
            "stat_bonuses": {"Health": 2162, "Speed": 434},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/accelerating_tint_lvl25.png"
        }
    },
    "tags_json": ["PictoType:Support", "LuminaType:Support", "Synergy:HealingTint", "AppliesStatus:Rush", "Buff:Ally"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "Aegis Revival", 
    "lumina_description": "Plus 1 Shield on being revived",
    "lumina_lp_cost": 5,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {
        "trigger": "on_self_revived",
        "applies_status_to_self": [{"name": "Shield", "stacks": 1}] # Assumes "Shield" is a stackable status
    },
    "picto_variants_json": {
        "12": {
            "stat_bonuses": {"Defense": 218, "Speed": 108},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/aegis_revival_lvl12.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Trigger:OnRevive", "AppliesStatus:Shield", "Buff:Self", "Mechanic:Survivability"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Anti-Blight", 
    "lumina_description": "Immune to Blight", 
    "lumina_lp_cost": 10,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {"grants_immunity_to_status": ["Blight"]},
    "picto_variants_json": {
        "20": { 
            "stat_bonuses": {"Health": 1333, "Defense": 647},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/anti-blight_lvl20.png"
        },
        "24": { 
            "stat_bonuses": {"Health": 1897, "Defense": 949},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/anti-blight_lvl24.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Mechanic:Immunity", "StatusEffect:Blight"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "Anti-Burn", 
    "lumina_description": "Immune to Burn",
    "lumina_lp_cost": 15,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {"grants_immunity_to_status": ["Burn"]},
    "picto_variants_json": {
        "29": {
            "stat_bonuses": {"Health": 2757, "Defense": 1572},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/anti-burn_lvl29.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Mechanic:Immunity", "StatusEffect:Burn"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "Anti-Charm", 
    "lumina_description": "Immune to Charm",
    "lumina_lp_cost": 10,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {"grants_immunity_to_status": ["Charm"]},
    "picto_variants_json": {
        "13": {
            "stat_bonuses": {"Health": 599, "Defense": 240},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/anti-charm_lvl13.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Mechanic:Immunity", "StatusEffect:Charm"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Anti-Freeze", 
    "lumina_description": "Immune to Freeze",
    "lumina_lp_cost": 15,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {"grants_immunity_to_status": ["Freeze"]},
    "picto_variants_json": {
        "21": {
            "stat_bonuses": {"Health": 1464, "Defense": 733},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/anti-freeze_lvl21.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Mechanic:Immunity", "StatusEffect:Freeze"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "Anti-Stun", 
    "lumina_description": "Immune to Stun",
    "lumina_lp_cost": 5, 
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {"grants_immunity_to_status": ["Stun"]},
    "picto_variants_json": {
        "29": { 
            "stat_bonuses": {"Health": 2757, "Defense": 1572}, 
            "acquisition_info": "", 
            "icon_url": "/static/pictos/anti-stun_lvl29.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Mechanic:Immunity", "StatusEffect:Stun"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "At Death's Door", 
    "lumina_description": "Deal 50% more damage if Health is below 10%",
    "lumina_lp_cost": 5,
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "condition": "self_health_below_percent", 
        "condition_value": 10,
        "effect_type": "damage_modifier", 
        "value": 1.5, # Assuming "50% more damage" is a 1.5x multiplier
        "operator": "multiply",
        "modifier_type": "MoreDamage" # Differentiating from "IncreasedDamage" based on status effect doc
        # TODO: Confirm if this is "MoreDamage" (multiplicative with all other sources) or "IncreasedDamage" (additive with similar sources).
    },
    "picto_variants_json": {
        "8": {
            "stat_bonuses": {"Defense": 96, "Crit_Rate_Percent": 11}, 
            "acquisition_info": "", 
            "icon_url": "/static/pictos/at_deaths_door_lvl8.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Condition:LowHealth", "Effect:DamageBoost", "Mechanic:HighRiskReward"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Attack Lifesteal", 
    "lumina_description": "Recover 15% Health on Base Attack",
    "lumina_lp_cost": 15,
    "lumina_type": "Defensive", 
    "lumina_effect_details_json": {
        "trigger": "on_base_attack",
        # Option 1: Heal is % of Max HP
        "effect_type": "heal_self", "basis": "max_hp", "value_percent": 15
        # Option 2: Heal is % of damage dealt by the base attack (Lifesteal)
        # "effect_type": "lifesteal", "basis": "damage_dealt_by_triggering_action", "value_percent": 15 
        # TODO: Clarify if heal is % Max HP (Option 1) or % damage dealt (Option 2). Defaulting to Max HP for now.
    },
    "picto_variants_json": {
        "4": {
            "stat_bonuses": {"Health": 88, "Crit_Rate_Percent": 8},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/attack_lifesteal_lvl4.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Trigger:OnBaseAttack", "Effect:HealSelf", "Mechanic:Sustain"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Augmented Aim", 
    "lumina_description": "50% increased Free Aim damage",
    "lumina_lp_cost": 3, # From your sheet, not the "?" in SB2 Value
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "damage_boost",
        "damage_source_type": "FreeAim", # Tag: DamageSource:FreeAim
        "value_percent": 50,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if this is "Increased" or "More" damage and how it stacks.
    },
    "picto_variants_json": {
        "3": { # Picto Level from your sheet
            "picto_display_name": "Augmented Aim Picto (Lvl 3)",
            "stat_bonuses": {"Speed": 21, "Crit_Rate_Percent": 4}, # Interpreted "Crit"
            "acquisition_info": "", 
            "icon_url": "/static/pictos/augmented_aim_lvl3.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageSource:FreeAim"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Augmented Attack", 
    "lumina_description": "50% increased Base Attack damage",
    "lumina_lp_cost": 7, # From your sheet
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "damage_boost",
        "damage_source_type": "BaseAttack", # Tag: DamageSource:BaseAttack
        "value_percent": 50,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if "Increased" or "More" damage.
    },
    "picto_variants_json": {
        "2": { 
            "picto_display_name": "Augmented Attack Picto (Lvl 2)",
            "stat_bonuses": {"Defense": 8, "Speed": 10},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/augmented_attack_lvl2.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageSource:BaseAttack", "Enhance:BaseAttack"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Augmented Counter I", # Distinct Picto name
    "lumina_description": "25% increased Counterattack damage",
    "lumina_lp_cost": 3, # From your sheet
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "damage_boost",
        "damage_source_type": "Counterattack", # Tag: DamageSource:Counterattack
        "value_percent": 25,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if "Increased" or "More" damage.
    },
    "picto_variants_json": {
        "8": { 
            "picto_display_name": "Augmented Counter I Picto (Lvl 8)",
            "stat_bonuses": {"Health": 385, "Crit_Rate_Percent": 6},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/augmented_counter_i_lvl8.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageSource:Counterattack", "AugmentedCounterSeries:1"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Augmented Counter II", # Distinct Picto name
    "lumina_description": "50% increased Counterattack damage",
    "lumina_lp_cost": 5, # From your sheet
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "damage_boost",
        "damage_source_type": "Counterattack",
        "value_percent": 50,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if "Increased" or "More" damage.
    },
    "picto_variants_json": {
        "12": { 
            "picto_display_name": "Augmented Counter II Picto (Lvl 12)",
            "stat_bonuses": {"Defense": 208, "Crit_Rate_Percent": 15},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/augmented_counter_ii_lvl12.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageSource:Counterattack", "AugmentedCounterSeries:2"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Augmented Counter III", # Distinct Picto name
    "lumina_description": "75% increased Counterattack damage",
    "lumina_lp_cost": 7, # From your sheet
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "damage_boost",
        "damage_source_type": "Counterattack",
        "value_percent": 75,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if "Increased" or "More" damage.
    },
    "picto_variants_json": {
        "17": { 
            "picto_display_name": "Augmented Counter III Picto (Lvl 17)",
            "stat_bonuses": {"Defense": 432, "Crit_Rate_Percent": 19},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/augmented_counter_iii_lvl17.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageSource:Counterattack", "AugmentedCounterSeries:3"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "Augmented First Strike", 
    "lumina_description": "50% increased damage on the first hit. Once per battle.",
    "lumina_lp_cost": 5,
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "conditional_damage_boost",
        "condition": "first_hit_dealt_in_battle",
        "value_percent": 50,
        "modifier_type": "MoreDamage", # Typically "first hit" bonuses are multiplicative
        "limit_per_battle": 1
        # TODO: Confirm if this applies to any first hit, or first hit by the character equipping this.
    },
    "picto_variants_json": {
        "6": { 
            "picto_display_name": "Augmented First Strike Picto (Lvl 6)",
            "stat_bonuses": {"Speed": 51, "Crit_Rate_Percent": 5},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/augmented_first_strike_lvl6.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "Condition:FirstHit", "Mechanic:OncePerBattle"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Auto Death", 
    "lumina_description": "Kills self on battle start",
    "lumina_lp_cost": 1,
    "lumina_type": "Support", # Type from sheet
    "lumina_effect_details_json": {
        "trigger": "on_battle_start",
        "effect_type": "self_defeat"
    },
    "picto_variants_json": {
        "7": { 
            "picto_display_name": "Auto Death Picto (Lvl 7)",
            "stat_bonuses": {"Crit_Rate_Percent": 26}, # SB1 Value used, SB2 Name "N/A" ignored
            "acquisition_info": "", 
            "icon_url": "/static/pictos/auto_death_lvl7.png"
        }
    },
    "tags_json": ["PictoType:Support", "LuminaType:Support", "Trigger:OnBattleStart", "Effect:SelfDefeat", "Mechanic:Sacrifice", "Synergy:AutoDeathBuild"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Auto Regen", 
    "lumina_description": "Apply Regen for 3 turns on battle start",
    "lumina_lp_cost": 10,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {
        "trigger": "on_battle_start",
        "applies_status_to_self": [{"name": "Regen", "duration_turns": 3}]
    },
    "picto_variants_json": {
        "13": { 
            "picto_display_name": "Auto Regen Picto (Lvl 13)",
            "stat_bonuses": {"Defense": 479}, # SB1 Value used, SB2 Name "N/A" ignored
            "acquisition_info": "", 
            "icon_url": "/static/pictos/auto_regen_lvl13.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Trigger:OnBattleStart", "AppliesStatus:Regen", "Buff:Self", "Mechanic:Sustain"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Auto Rush", 
    "lumina_description": "Apply Rush for 3 turns on battle start",
    "lumina_lp_cost": 10,
    "lumina_type": "Offensive", # Type from sheet
    "lumina_effect_details_json": {
        "trigger": "on_battle_start",
        "applies_status_to_self": [{"name": "Rush", "duration_turns": 3}]
    },
    "picto_variants_json": {
        "10": { 
            "picto_display_name": "Auto Rush Picto (Lvl 10)",
            "stat_bonuses": {"Speed": 112, "Crit_Rate_Percent": 7},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/auto_rush_lvl10.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Trigger:OnBattleStart", "AppliesStatus:Rush", "Buff:Self", "Mechanic:SpeedBoost"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Auto Shell", 
    "lumina_description": "Apply Shell for 3 turns on battle start",
    "lumina_lp_cost": 10,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {
        "trigger": "on_battle_start",
        "applies_status_to_self": [{"name": "Shell", "duration_turns": 3}]
    },
    "picto_variants_json": {
        "7": { 
            "picto_display_name": "Auto Shell Picto (Lvl 7)",
            "stat_bonuses": {"Health": 411}, # SB1 Value used, SB2 Name "N/A" ignored
            "acquisition_info": "", 
            "icon_url": "/static/pictos/auto_shell_lvl7.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Trigger:OnBattleStart", "AppliesStatus:Shell", "Buff:Self", "Mechanic:DamageReduction"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Base Shield", 
    "lumina_description": "Plus 1 Shield if not affected by any Shield on turn start",
    "lumina_lp_cost": 20,
    "lumina_type": "Defensive",
    "lumina_effect_details_json": {
        "trigger": "on_turn_start",
        "condition": "self_not_affected_by_status_shield", # Assumes "Shield" is the status name
        "applies_status_to_self": [{"name": "Shield", "stacks": 1}]
    },
    "picto_variants_json": {
        "20": { 
            "picto_display_name": "Base Shield Picto (Lvl 20)",
            "stat_bonuses": {"Speed": 378, "Crit_Rate_Percent": 11},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/base_shield_lvl20.png"
        }
    },
    "tags_json": ["PictoType:Defensive", "LuminaType:Defensive", "Trigger:OnTurnStart", "AppliesStatus:Shield", "Buff:Self", "Condition:NoShield"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "Beneficial Contamination", 
    "lumina_description": "Plus 2 AP on applying a Status Effect. Once per turn.",
    "lumina_lp_cost": 15,
    "lumina_type": "Support",
    "lumina_effect_details_json": {
        "trigger": "on_applying_any_status_effect", # Could be more specific if it's only debuffs or only buffs
        "effect_type": "gain_ap",
        "value": 2,
        "target": "self",
        "limit_per_turn": 1
    },
    "picto_variants_json": {
        "14": { 
            "picto_display_name": "Beneficial Contamination Picto (Lvl 14)",
            "stat_bonuses": {"Defense": 274, "Speed": 135},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/beneficial_contamination_lvl14.png"
        }
    },
    "tags_json": ["PictoType:Support", "LuminaType:Support", "Trigger:OnApplyStatusEffect", "Mechanic:APGeneration", "Mechanic:OncePerTurn"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Breaker", 
    "lumina_description": "25% increased Break damage",
    "lumina_lp_cost": 10,
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "damage_boost",
        "damage_category": "Break", # Tag: DamageType:Break
        "value_percent": 25,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if "Increased" or "More".
    },
    "picto_variants_json": {
        "5": { 
            "picto_display_name": "Breaker Picto (Lvl 5)",
            "stat_bonuses": {"Speed": 26, "Crit_Rate_Percent": 9},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/breaker_lvl5.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageType:Break", "Mechanic:Break"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Breaking Attack", 
    "lumina_description": "Base Attack can Break",
    "lumina_lp_cost": 10,
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "modifies_action": "BaseAttack",
        "grants_property": "CanBreak" # Tag: Mechanic:Break
    },
    "picto_variants_json": {
        "15": { 
            "picto_display_name": "Breaking Attack Picto (Lvl 15)",
            "stat_bonuses": {"Speed": 154, "Crit_Rate_Percent": 17},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/breaking_attack_lvl15.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Enhance:BaseAttack", "Mechanic:Break"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Breaking Burn", 
    "lumina_description": "25% increased Break damage on Burning enemies",
    "lumina_lp_cost": 5,
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "conditional_damage_boost",
        "damage_category": "Break",
        "condition": "target_is_burning", # Tag: Condition:TargetBurning
        "value_percent": 25,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if "Increased" or "More".
    },
    "picto_variants_json": {
        "15": { 
            "picto_display_name": "Breaking Burn Picto (Lvl 15)",
            "stat_bonuses": {"Speed": 243, "Crit_Rate_Percent": 9},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/breaking_burn_lvl15.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageType:Break", "Condition:TargetBurning", "Synergy:BurnBuild"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Breaking Counter", 
    "lumina_description": "50% increased Break damage on Counterattack",
    "lumina_lp_cost": 3,
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "conditional_damage_boost",
        "damage_category": "Break",
        "condition": "on_counterattack", # Tag: Trigger:OnCounterattack
        "value_percent": 50,
        "modifier_type": "IncreasedDamage" # TODO: Confirm if "Increased" or "More".
    },
    "picto_variants_json": {
        "7": { 
            "picto_display_name": "Breaking Counter Picto (Lvl 7)",
            "stat_bonuses": {"Speed": 43, "Crit_Rate_Percent": 10},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/breaking_counter_lvl7.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageType:Break", "Trigger:OnCounterattack", "Synergy:CounterattackBuild"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Breaking Death", 
    "lumina_description": "Fully charge enemy's Break bar on death",
    "lumina_lp_cost": 5,
    "lumina_type": "Support", # Could be Offensive depending on how "Break bar" works
    "lumina_effect_details_json": {
        "trigger": "on_own_death", # Assuming self-death, like other "Death" pictos
        "effect_type": "charge_enemy_break_bar",
        "value": "full"
        # TODO: Clarify if "Break bar" means Shields or a Stagger/Stun gauge. This affects its tags and synergy.
    },
    "picto_variants_json": {
        "29": { 
            "picto_display_name": "Breaking Death Picto (Lvl 29)",
            "stat_bonuses": {"Speed": 586, "Crit_Rate_Percent": 33},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/breaking_death_lvl29.png"
        }
    },
    "tags_json": ["PictoType:Support", "LuminaType:Support", "Trigger:OnDeath", "Mechanic:BreakCharge", "Synergy:AutoDeathBuild"],
    "spoiler_info_json": {"act_available": 2} 
},
{
    "name": "Breaking Shots", 
    "lumina_description": "50% increased Break damage with Free Aim shots",
    "lumina_lp_cost": 1,
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "conditional_damage_boost",
        "damage_category": "Break",
        "condition": "on_free_aim_shot", # Tag: DamageSource:FreeAim
        "value_percent": 50,
        "modifier_type": "IncreasedDamage" # TODO: Confirm.
    },
    "picto_variants_json": {
        "7": { 
            "picto_display_name": "Breaking Shots Picto (Lvl 7)",
            "stat_bonuses": {"Speed": 43, "Crit_Rate_Percent": 10},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/breaking_shots_lvl7.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageType:Break", "DamageSource:FreeAim"],
    "spoiler_info_json": {"act_available": 1} 
},
{
    "name": "Breaking Slow", 
    "lumina_description": "25% increased Break damage against Slowed enemies",
    "lumina_lp_cost": 0, # LP Cost column has "??", assuming 0 or needs clarification
    "lumina_type": "Offensive",
    "lumina_effect_details_json": {
        "effect_type": "conditional_damage_boost",
        "damage_category": "Break",
        "condition": "target_is_slowed", # Tag: Condition:TargetSlowed
        "value_percent": 25,
        "modifier_type": "IncreasedDamage" # TODO: Confirm.
        # TODO: LP Cost is "??". Defaulting to 0 for now, please verify.
    },
    "picto_variants_json": {
        "15": { 
            "picto_display_name": "Breaking Slow Picto (Lvl 15)",
            "stat_bonuses": {"Speed": 162, "Crit_Rate_Percent": 17},
            "acquisition_info": "", 
            "icon_url": "/static/pictos/breaking_slow_lvl15.png"
        }
    },
    "tags_json": ["PictoType:Offensive", "LuminaType:Offensive", "Effect:DamageBoost", "DamageType:Break", "Condition:TargetSlowed", "Synergy:Slow"],
    "spoiler_info_json": {"act_available": 1} 
}
    
]