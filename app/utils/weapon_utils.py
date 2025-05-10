"""
Utility functions for weapon calculations.
"""

def calculate_weapon_stats(weapon, level):
    """
    Calculate the power and attribute scaling of a weapon based on its current level.

    Args:
        weapon (dict): The weapon data.
        level (int): The current level of the weapon.

    Returns:
        dict: A dictionary containing the calculated power and attributes.
    """
    max_level = weapon.get("max_level", 33)
    power_scaling = weapon.get("power_scaling", {})
    attribute_scaling = weapon.get("attribute_scaling", {})

    # Calculate power
    base_power = power_scaling.get("base", 0)
    max_power = power_scaling.get("max", 0)
    power = base_power + (max_power - base_power) * (level - 1) / (max_level - 1)

    # Calculate attributes
    attributes = {}
    for attr, scaling in attribute_scaling.items():
        base_grade = scaling.get("base")
        max_grade = scaling.get("max")
        if base_grade and max_grade:
            # Map grades to numerical values for interpolation
            grade_map = {"C": 1, "B": 2, "A": 3, "S": 4}
            base_value = grade_map.get(base_grade, 0)
            max_value = grade_map.get(max_grade, 0)
            interpolated_value = base_value + (max_value - base_value) * (level - 1) / (max_level - 1)

            # Map back to grades
            reverse_grade_map = {v: k for k, v in grade_map.items()}
            attributes[attr] = reverse_grade_map.get(round(interpolated_value), base_grade)

    return {
        "power": round(power),
        "attributes": attributes
    }
