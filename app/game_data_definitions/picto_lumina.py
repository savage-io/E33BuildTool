PICTOS_LUMINAS_DEFINITIONS = [
{
    "name": "Accelerating Heal", # Conceptual Name
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
}
]