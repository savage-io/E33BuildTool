from flask import Blueprint, request, jsonify
from . import db
from .models import GameCharacterCOE33, SkillCOE33  # Ensure SkillCOE33 is imported

# Create a Blueprint for organizing API routes
bp = Blueprint('main', __name__, url_prefix='/api/coe33')

# --- GameCharacterCOE33 CRUD Endpoints ---
# (Your existing GameCharacterCOE33 endpoints should already be here)

# --- SkillCOE33 CRUD Endpoints ---

@bp.route('/skills', methods=['POST'])
def create_skill():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('description'):
        return jsonify({'error': 'Skill name and description are required'}), 400

    # Optional: Check for existing skill by name if names should be unique
    # if SkillCOE33.query.filter_by(name=data['name']).first():
    #     return jsonify({'error': f"Skill with name '{data['name']}' already exists."}), 409

    new_skill = SkillCOE33(
        name=data['name'],
        description=data['description'],
        ap_cost=data.get('ap_cost'),
        effects_json=data.get('effects_json'),  # e.g., {"damage": 50, "type": "melee", "status_effect": "stun"}
        icon_url=data.get('icon_url')
        # If you decide skills are character-specific via character_id FK:
        # character_id=data.get('character_id')
    )
    db.session.add(new_skill)
    db.session.commit()
    return jsonify({'message': 'Skill created successfully', 'skill_id': new_skill.id}), 201

@bp.route('/skills', methods=['GET'])
def get_all_skills():
    skills = SkillCOE33.query.all()
    skill_list = []
    for skill in skills:
        skill_list.append({
            'id': skill.id,
            'name': skill.name,
            'description': skill.description,
            'ap_cost': skill.ap_cost,
            'effects_json': skill.effects_json,
            'icon_url': skill.icon_url
            # 'character_id': skill.character_id # If applicable
        })
    return jsonify(skill_list), 200

@bp.route('/skills/<int:skill_id>', methods=['GET'])
def get_skill(skill_id):
    skill = SkillCOE33.query.get_or_404(skill_id)
    return jsonify({
        'id': skill.id,
        'name': skill.name,
        'description': skill.description,
        'ap_cost': skill.ap_cost,
        'effects_json': skill.effects_json,
        'icon_url': skill.icon_url
        # 'character_id': skill.character_id # If applicable
    }), 200

@bp.route('/skills/<int:skill_id>', methods=['PUT'])
def update_skill(skill_id):
    skill = SkillCOE33.query.get_or_404(skill_id)
    data = request.get_json()

    skill.name = data.get('name', skill.name)
    skill.description = data.get('description', skill.description)
    skill.ap_cost = data.get('ap_cost', skill.ap_cost)
    skill.effects_json = data.get('effects_json', skill.effects_json)
    skill.icon_url = data.get('icon_url', skill.icon_url)
    # if 'character_id' in data: # If applicable
    #     skill.character_id = data.get('character_id')

    db.session.commit()
    return jsonify({'message': f'Skill {skill.name} updated successfully'}), 200

@bp.route('/skills/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    skill = SkillCOE33.query.get_or_404(skill_id)
    # Consider implications: what happens to builds using this skill?
    # For now, a simple delete.
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': f'Skill {skill.name} deleted successfully'}), 200