from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.municipality_schema import expected_fields_create

municipality_routes = Blueprint('municipality', __name__)

#Method for create person.
@municipality_routes.route('/createMunicipality',methods=['POST'])
#@jwt_required()
def create_municipality():

    try:        
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        municipalityCreate = service_manager.municipality_service.create_municipality(data, 'root')#get_jwt_identity())
        if municipalityCreate is None:
            return jsonify({'error': 'Internal Server'}), 500   
        
        return jsonify({'message': 'Municipality created'}), 201
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500    