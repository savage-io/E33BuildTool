from flask import Blueprint, request, jsonify, Response, json
from . import db
from .models import GameCharacterCOE33, SkillCOE33, PictoLumina, Weapon  # Updated import
from sqlalchemy import or_  # Import or_ for query filtering

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

@bp.route('/skills', methods=['GET'])
def get_skills():
    """Fetch skills filtered by user_max_act."""
    user_max_act = request.args.get('user_max_act', default=99, type=int)

    # Query for skills
    skills_query = SkillCOE33.query.filter(
        or_(
            SkillCOE33.spoiler_info_json == None,
            SkillCOE33.spoiler_info_json["act_available"].astext.cast(db.Integer) <= user_max_act
        )
    )

    skills = skills_query.all()

    # Serialize skills for response
    skills_data = [
        {
            "name": skill.name,
            "description": skill.description,
            "ap_cost": skill.ap_cost,
            "tags": skill.tags_json,
            "spoiler_info": skill.spoiler_info_json
        }
        for skill in skills
    ]

    return jsonify(skills_data)

# --- PictoLumina CRUD Endpoints ---

@bp.route('/pictos', methods=['POST'])
def create_picto():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('lumina_description'):
        return jsonify({'error': 'Picto name and lumina description are required'}), 400

    new_picto = PictoLumina(
        name=data['name'],
        lumina_description=data['lumina_description'],
        lumina_lp_cost=data.get('lumina_lp_cost'),
        lumina_type=data.get('lumina_type'),
        lumina_effect_details_json=data.get('lumina_effect_details_json'),
        picto_variants_json=data.get('picto_variants_json'),
        tags_json=data.get('tags_json'),
        spoiler_info_json=data.get('spoiler_info_json')
    )
    db.session.add(new_picto)
    db.session.commit()
    return jsonify({'message': 'Picto created successfully', 'picto_id': new_picto.id}), 201

@bp.route('/pictos', methods=['GET'])
def get_all_pictos():
    pictos = PictoLumina.query.all()
    picto_list = []
    for picto in pictos:
        picto_list.append({
            'id': picto.id,
            'name': picto.name,
            'lumina_description': picto.lumina_description,
            'lumina_lp_cost': picto.lumina_lp_cost,
            'lumina_type': picto.lumina_type,
            'lumina_effect_details_json': picto.lumina_effect_details_json,
            'picto_variants_json': picto.picto_variants_json,
            'tags_json': picto.tags_json,
            'spoiler_info_json': picto.spoiler_info_json
        })
    return jsonify(picto_list), 200

@bp.route('/pictos/<int:picto_id>', methods=['GET'])
def get_picto(picto_id):
    picto = PictoLumina.query.get_or_404(picto_id)
    return jsonify({
        'id': picto.id,
        'name': picto.name,
        'lumina_description': picto.lumina_description,
        'lumina_lp_cost': picto.lumina_lp_cost,
        'lumina_type': picto.lumina_type,
        'lumina_effect_details_json': picto.lumina_effect_details_json,
        'picto_variants_json': picto.picto_variants_json,
        'tags_json': picto.tags_json,
        'spoiler_info_json': picto.spoiler_info_json
    }), 200

@bp.route('/pictos/<int:picto_id>', methods=['PUT'])
def update_picto(picto_id):
    picto = PictoLumina.query.get_or_404(picto_id)
    data = request.get_json()

    picto.name = data.get('name', picto.name)
    picto.lumina_description = data.get('lumina_description', picto.lumina_description)
    picto.lumina_lp_cost = data.get('lumina_lp_cost', picto.lumina_lp_cost)
    picto.lumina_type = data.get('lumina_type', picto.lumina_type)
    picto.lumina_effect_details_json = data.get('lumina_effect_details_json', picto.lumina_effect_details_json)
    picto.picto_variants_json = data.get('picto_variants_json', picto.picto_variants_json)
    picto.tags_json = data.get('tags_json', picto.tags_json)
    picto.spoiler_info_json = data.get('spoiler_info_json', picto.spoiler_info_json)

    db.session.commit()
    return jsonify({'message': f'Picto {picto.name} updated successfully'}), 200

@bp.route('/pictos/<int:picto_id>', methods=['DELETE'])
def delete_picto(picto_id):
    picto = PictoLumina.query.get_or_404(picto_id)
    db.session.delete(picto)
    db.session.commit()
    return jsonify({'message': f'Picto {picto.name} deleted successfully'}), 200

@bp.route('/pictos', methods=['GET'])
def get_filtered_pictos():
    """Fetch pictos filtered by user_max_act."""
    user_max_act = request.args.get('user_max_act', default=99, type=int)

    # Query for pictos
    pictos_query = PictoLumina.query.filter(
        or_(
            PictoLumina.spoiler_info_json == None,
            PictoLumina.spoiler_info_json["act_available"].astext.cast(db.Integer) <= user_max_act
        )
    )

    pictos = pictos_query.all()

    # Serialize pictos for response
    pictos_data = [
        {
            "id": picto.id,
            "name": picto.name,
            "lumina_description": picto.lumina_description,
            "lumina_lp_cost": picto.lumina_lp_cost,
            "lumina_type": picto.lumina_type,
            "lumina_effect_details_json": picto.lumina_effect_details_json,
            "picto_variants_json": picto.picto_variants_json,
            "tags_json": picto.tags_json,
            "spoiler_info_json": picto.spoiler_info_json
        }
        for picto in pictos
    ]

    return jsonify(pictos_data)

# --- LuminaCOE33 CRUD Endpoints ---

@bp.route('/luminas', methods=['POST'])
def create_lumina():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('lumina_description'):
        return jsonify({'error': 'Lumina name and description are required'}), 400

    new_lumina = PictoLumina(
        name=data['name'],
        lumina_description=data['lumina_description'],
        lumina_lp_cost=data.get('lumina_lp_cost'),
        lumina_type=data.get('lumina_type'),
        lumina_effect_details_json=data.get('lumina_effect_details_json'),
        tags_json=data.get('tags_json'),
        spoiler_info_json=data.get('spoiler_info_json')
    )
    db.session.add(new_lumina)
    db.session.commit()
    return jsonify({'message': 'Lumina created successfully', 'lumina_id': new_lumina.id}), 201

@bp.route('/luminas', methods=['GET'])
def get_all_luminas():
    luminas = PictoLumina.query.all()
    lumina_list = []
    for lumina in luminas:
        lumina_list.append({
            'id': lumina.id,
            'name': lumina.name,
            'lumina_description': lumina.lumina_description,
            'lumina_lp_cost': lumina.lumina_lp_cost,
            'lumina_type': lumina.lumina_type,
            'lumina_effect_details_json': lumina.lumina_effect_details_json,
            'tags_json': lumina.tags_json,
            'spoiler_info_json': lumina.spoiler_info_json
        })
    return jsonify(lumina_list), 200

@bp.route('/luminas/<int:lumina_id>', methods=['GET'])
def get_lumina(lumina_id):
    lumina = PictoLumina.query.get_or_404(lumina_id)
    return jsonify({
        'id': lumina.id,
        'name': lumina.name,
        'lumina_description': lumina.lumina_description,
        'lumina_lp_cost': lumina.lumina_lp_cost,
        'lumina_type': lumina.lumina_type,
        'lumina_effect_details_json': lumina.lumina_effect_details_json,
        'tags_json': lumina.tags_json,
        'spoiler_info_json': lumina.spoiler_info_json
    }), 200

@bp.route('/luminas/<int:lumina_id>', methods=['PUT'])
def update_lumina(lumina_id):
    lumina = PictoLumina.query.get_or_404(lumina_id)
    data = request.get_json()

    lumina.name = data.get('name', lumina.name)
    lumina.lumina_description = data.get('lumina_description', lumina.lumina_description)
    lumina.lumina_lp_cost = data.get('lumina_lp_cost', lumina.lumina_lp_cost)
    lumina.lumina_type = data.get('lumina_type', lumina.lumina_type)
    lumina.lumina_effect_details_json = data.get('lumina_effect_details_json', lumina.lumina_effect_details_json)
    lumina.tags_json = data.get('tags_json', lumina.tags_json)
    lumina.spoiler_info_json = data.get('spoiler_info_json', lumina.spoiler_info_json)

    db.session.commit()
    return jsonify({'message': f'Lumina {lumina.name} updated successfully'}), 200

@bp.route('/luminas/<int:lumina_id>', methods=['DELETE'])
def delete_lumina(lumina_id):
    lumina = PictoLumina.query.get_or_404(lumina_id)
    db.session.delete(lumina)
    db.session.commit()
    return jsonify({'message': f'Lumina {lumina.name} deleted successfully'}), 200

@bp.route('/luminas', methods=['GET'])
def get_filtered_luminas():
    """Fetch luminas filtered by user_max_act."""
    user_max_act = request.args.get('user_max_act', default=99, type=int)

    # Query for luminas
    luminas_query = PictoLumina.query.filter(
        or_(
            PictoLumina.spoiler_info_json == None,
            PictoLumina.spoiler_info_json["act_available"].astext.cast(db.Integer) <= user_max_act
        )
    )

    luminas = luminas_query.all()

    # Serialize luminas for response
    luminas_data = [
        {
            "id": lumina.id,
            "name": lumina.name,
            "lumina_description": lumina.lumina_description,
            "lumina_lp_cost": lumina.lumina_lp_cost,
            "lumina_type": lumina.lumina_type,
            "lumina_effect_details_json": lumina.lumina_effect_details_json,
            "tags_json": lumina.tags_json,
            "spoiler_info_json": lumina.spoiler_info_json
        }
        for lumina in luminas
    ]

    return jsonify(luminas_data)

@bp.route('/weapons', methods=['GET'])
def get_weapons():
    """Fetch all weapons data."""

    weapons = Weapon.query.all()
    weapons_data = [
        {
            "id": weapon.id,
            "name": weapon.name,
            "weapons_type": weapon.weapons_type,
            "element": weapon.element,
            "power_by_level_json": weapon.power_by_level_json,
            "attribute_scaling_tiers_json": weapon.attribute_scaling_tiers_json,
            "passive_effects_by_level_json": weapon.passive_effects_by_level_json,
            "acquisition_info": weapon.acquisition_info,
            "icon_url": weapon.icon_url,
            "primary_character_name": weapon.primary_character_name,
            "metadata_json": weapon.metadata_json
        }
        for weapon in weapons
    ]
    return Response(json.dumps(weapons_data, sort_keys=False), mimetype='application/json')

@bp.route('/weapons', methods=['GET'])
def get_filtered_weapons():
    """Fetch weapons filtered by user_max_act."""
    user_max_act = request.args.get('user_max_act', default=99, type=int)

    # Query for weapons
    weapons_query = Weapon.query.filter(
        or_(
            Weapon.spoiler_info_json == None,
            Weapon.spoiler_info_json["act_available"].astext.cast(db.Integer) <= user_max_act
        )
    )

    weapons = weapons_query.all()

    # Serialize weapons for response
    weapons_data = [
        {
            "id": weapon.id,
            "name": weapon.name,
            "weapons_type": weapon.weapons_type,
            "element": weapon.element,
            "power_by_level_json": weapon.power_by_level_json,
            "attribute_scaling_tiers_json": weapon.attribute_scaling_tiers_json,
            "passive_effects_by_level_json": weapon.passive_effects_by_level_json,
            "acquisition_info": weapon.acquisition_info,
            "icon_url": weapon.icon_url,
            "primary_character_name": weapon.primary_character_name,
            "metadata_json": weapon.metadata_json,
            "spoiler_info": weapon.spoiler_info_json
        }
        for weapon in weapons
    ]

    return jsonify(weapons_data)

@bp.route('/characters', methods=['GET'])
def get_filtered_characters():
    """Fetch characters filtered by user_max_act."""
    user_max_act = request.args.get('user_max_act', default=99, type=int)

    # Query for characters
    characters_query = GameCharacterCOE33.query.filter(
        or_(
            GameCharacterCOE33.spoiler_info_json == None,
            GameCharacterCOE33.spoiler_info_json["act_available"].astext.cast(db.Integer) <= user_max_act
        )
    )

    characters = characters_query.all()

    # Serialize characters for response
    characters_data = [
        {
            "name": character.name,
            "description": character.description,
            "base_stats_json": character.base_stats_json,
            "unique_mechanic_description": character.unique_mechanic_description,
            "icon_url": character.icon_url,
            "spoiler_info": character.spoiler_info_json
        }
        for character in characters
    ]

    return jsonify(characters_data)

@bp.route('/pictos_luminas', methods=['GET'])
def get_pictos_luminas():
    """Fetches Picto Lumina data, filterable by type."""
    lumina_type = request.args.get('type')

    query = PictoLumina.query
    if lumina_type:
        query = query.filter(PictoLumina.lumina_type == lumina_type)

    results = query.all()
    response_data = [
        {
            'id': item.id,
            'name': item.name,
            'lumina_description': item.lumina_description,
            'lumina_lp_cost': item.lumina_lp_cost,
            'lumina_type': item.lumina_type,
            'lumina_effect_details_json': item.lumina_effect_details_json,
            'picto_variants_json': item.picto_variants_json,
            'tags_json': item.tags_json,
            'spoiler_info_json': item.spoiler_info_json
        }
        for item in results
    ]

    return jsonify(response_data), 200