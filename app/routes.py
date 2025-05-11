from flask import Blueprint, request, jsonify, Response, json
from . import db
from .models import GameCharacterCOE33, SkillCOE33, PictoCOE33, LuminaCOE33  # Ensure SkillCOE33 is imported

# Create a Blueprint for organizing API routes
bp = Blueprint('main', __name__, url_prefix='/api/coe33')

# --- GameCharacterCOE33 CRUD Endpoints ---

@bp.route('/characters', methods=['POST'])
def create_character():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Character name is required'}), 400

    if GameCharacterCOE33.query.filter_by(name=data['name']).first():
        return jsonify({'error': f"Character with name '{data['name']}' already exists."}), 409

    new_character = GameCharacterCOE33(
        name=data['name'],
        description=data.get('description'),
        base_stats_json=data.get('base_stats_json'),
        unique_mechanic_description=data.get('unique_mechanic_description'),
        icon_url=data.get('icon_url')
    )
    db.session.add(new_character)
    db.session.commit()
    return jsonify({'message': 'Character created successfully', 'character_id': new_character.id}), 201

@bp.route('/characters', methods=['GET'])
def get_all_characters():
    characters = GameCharacterCOE33.query.all()
    character_list = []
    for char in characters:
        character_list.append({
            'name': char.name,
            'description': char.description,
            'base_stats_json': char.base_stats_json,
            'unique_mechanic_description': char.unique_mechanic_description,
            'icon_url': char.icon_url
        })
    return jsonify(character_list), 200

@bp.route('/characters/<string:character_name>', methods=['GET'])
def get_character(character_name):
    character = GameCharacterCOE33.query.filter_by(name=character_name).first_or_404()
    return jsonify({
        'name': character.name,
        'description': character.description,
        'base_stats_json': character.base_stats_json,
        'unique_mechanic_description': character.unique_mechanic_description,
        'icon_url': character.icon_url
    }), 200

@bp.route('/characters/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    character = GameCharacterCOE33.query.get_or_404(character_id)
    data = request.get_json()

    if 'name' in data:
        existing_character = GameCharacterCOE33.query.filter(GameCharacterCOE33.name == data['name'], GameCharacterCOE33.id != character_id).first()
        if existing_character:
            return jsonify({'error': f"Another character with name '{data['name']}' already exists."}), 409
        character.name = data['name']

    character.description = data.get('description', character.description)
    character.base_stats_json = data.get('base_stats_json', character.base_stats_json)
    character.unique_mechanic_description = data.get('unique_mechanic_description', character.unique_mechanic_description)
    character.icon_url = data.get('icon_url', character.icon_url)

    db.session.commit()
    return jsonify({'message': f'Character {character.name} updated successfully'}), 200

@bp.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = GameCharacterCOE33.query.get_or_404(character_id)
    db.session.delete(character)
    db.session.commit()
    return jsonify({'message': f'Character {character.name} deleted successfully'}), 200

# --- SkillCOE33 CRUD Endpoints ---

@bp.route('/skills', methods=['POST'])
def create_skill():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('description'):
        return jsonify({'error': 'Skill name and description are required'}), 400

    new_skill = SkillCOE33(
        name=data['name'],
        description=data['description'],
        ap_cost=data.get('ap_cost'),
        effects_json=data.get('effects_json'),
        icon_url=data.get('icon_url')
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

    db.session.commit()
    return jsonify({'message': f'Skill {skill.name} updated successfully'}), 200

@bp.route('/skills/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    skill = SkillCOE33.query.get_or_404(skill_id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': f'Skill {skill.name} deleted successfully'}), 200

# --- PictoCOE33 CRUD Endpoints ---

@bp.route('/pictos', methods=['POST'])
def create_picto():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('description'):
        return jsonify({'error': 'Picto name and description are required'}), 400

    new_picto = PictoCOE33(
        name=data['name'],
        description=data['description'],
        stat_bonuses_json=data.get('stat_bonuses_json'),
        associated_lumina_id=data.get('associated_lumina_id'),
        how_to_acquire=data.get('how_to_acquire'),
        icon_url=data.get('icon_url')
    )
    db.session.add(new_picto)
    db.session.commit()
    return jsonify({'message': 'Picto created successfully', 'picto_id': new_picto.id}), 201

@bp.route('/pictos', methods=['GET'])
def get_all_pictos():
    pictos = PictoCOE33.query.all()
    picto_list = []
    for picto in pictos:
        picto_list.append({
            'id': picto.id,
            'name': picto.name,
            'description': picto.description,
            'stat_bonuses_json': picto.stat_bonuses_json,
            'associated_lumina_id': picto.associated_lumina_id,
            'how_to_acquire': picto.how_to_acquire,
            'icon_url': picto.icon_url
        })
    return jsonify(picto_list), 200

@bp.route('/pictos/<int:picto_id>', methods=['GET'])
def get_picto(picto_id):
    picto = PictoCOE33.query.get_or_404(picto_id)
    return jsonify({
        'id': picto.id,
        'name': picto.name,
        'description': picto.description,
        'stat_bonuses_json': picto.stat_bonuses_json,
        'associated_lumina_id': picto.associated_lumina_id,
        'how_to_acquire': picto.how_to_acquire,
        'icon_url': picto.icon_url
    }), 200

@bp.route('/pictos/<int:picto_id>', methods=['PUT'])
def update_picto(picto_id):
    picto = PictoCOE33.query.get_or_404(picto_id)
    data = request.get_json()

    picto.name = data.get('name', picto.name)
    picto.description = data.get('description', picto.description)
    picto.stat_bonuses_json = data.get('stat_bonuses_json', picto.stat_bonuses_json)
    picto.associated_lumina_id = data.get('associated_lumina_id', picto.associated_lumina_id)
    picto.how_to_acquire = data.get('how_to_acquire', picto.how_to_acquire)
    picto.icon_url = data.get('icon_url', picto.icon_url)

    db.session.commit()
    return jsonify({'message': f'Picto {picto.name} updated successfully'}), 200

@bp.route('/pictos/<int:picto_id>', methods=['DELETE'])
def delete_picto(picto_id):
    picto = PictoCOE33.query.get_or_404(picto_id)
    db.session.delete(picto)
    db.session.commit()
    return jsonify({'message': f'Picto {picto.name} deleted successfully'}), 200

# --- LuminaCOE33 CRUD Endpoints ---

@bp.route('/luminas', methods=['POST'])
def create_lumina():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('description') or data.get('lumina_point_cost') is None:
        return jsonify({'error': 'Lumina name, description, and lumina_point_cost are required'}), 400

    new_lumina = LuminaCOE33(
        name=data['name'],
        description=data['description'],
        lumina_point_cost=data['lumina_point_cost'],
        effect_details_json=data.get('effect_details_json'),
        icon_url=data.get('icon_url')
    )
    db.session.add(new_lumina)
    db.session.commit()
    return jsonify({'message': 'Lumina created successfully', 'lumina_id': new_lumina.id}), 201

@bp.route('/luminas', methods=['GET'])
def get_all_luminas():
    luminas = LuminaCOE33.query.all()
    lumina_list = []
    for lumina in luminas:
        lumina_list.append({
            'id': lumina.id,
            'name': lumina.name,
            'description': lumina.description,
            'lumina_point_cost': lumina.lumina_point_cost,
            'effect_details_json': lumina.effect_details_json,
            'icon_url': lumina.icon_url
        })
    return jsonify(lumina_list), 200

@bp.route('/luminas/<int:lumina_id>', methods=['GET'])
def get_lumina(lumina_id):
    lumina = LuminaCOE33.query.get_or_404(lumina_id)
    return jsonify({
        'id': lumina.id,
        'name': lumina.name,
        'description': lumina.description,
        'lumina_point_cost': lumina.lumina_point_cost,
        'effect_details_json': lumina.effect_details_json,
        'icon_url': lumina.icon_url
    }), 200

@bp.route('/luminas/<int:lumina_id>', methods=['PUT'])
def update_lumina(lumina_id):
    lumina = LuminaCOE33.query.get_or_404(lumina_id)
    data = request.get_json()

    lumina.name = data.get('name', lumina.name)
    lumina.description = data.get('description', lumina.description)
    lumina.lumina_point_cost = data.get('lumina_point_cost', lumina.lumina_point_cost)
    lumina.effect_details_json = data.get('effect_details_json', lumina.effect_details_json)
    lumina.icon_url = data.get('icon_url', lumina.icon_url)

    db.session.commit()
    return jsonify({'message': f'Lumina {lumina.name} updated successfully'}), 200

@bp.route('/luminas/<int:lumina_id>', methods=['DELETE'])
def delete_lumina(lumina_id):
    lumina = LuminaCOE33.query.get_or_404(lumina_id)
    db.session.delete(lumina)
    db.session.commit()
    return jsonify({'message': f'Lumina {lumina.name} deleted successfully'}), 200

@bp.route('/weapons', methods=['GET'])
def get_weapons():
    """Fetch all weapons data."""
    from .models import Item

    weapons = Item.query.all()
    weapons_data = [
        {
            "id": weapon.id,
            "name": weapon.name,
            "item_type": weapon.item_type,
            "element": weapon.element,
            "power_by_level_json": weapon.power_by_level_json,
            "attribute_scaling_tiers_json": weapon.attribute_scaling_tiers_json,
            "passive_effects_by_level_json": weapon.passive_effects_by_level_json,
            "acquisition_info": weapon.acquisition_info,
            "icon_url": weapon.icon_url,
            "primary_character_name": weapon.primary_character_name,
            "metadata_json": weapon.metadata_json,
        }
        for weapon in weapons
    ]
    return Response(json.dumps(weapons_data, sort_keys=False), mimetype='application/json')