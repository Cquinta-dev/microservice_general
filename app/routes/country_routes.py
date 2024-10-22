from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.country_schema import expected_fields_create

country_routes = Blueprint('country', __name__)

#Method for create country.
@country_routes.route('/createCountry',methods=['POST'])
#@jwt_required()
def create_country():

    try:        
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        countryCreate = service_manager.country_service.create_country(data, 'root')#get_jwt_identity())
        if countryCreate is None:
            return jsonify({'error': 'Internal Server'}), 500   
        
        return jsonify({'message': 'Country created'}), 201
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500    