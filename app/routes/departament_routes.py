from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.departament_schema import expected_fields_create

departament_routes = Blueprint('departament', __name__)

#Method for create person.
@departament_routes.route('/createDepartament',methods=['POST'])
#@jwt_required()
def create_departament():

    try:        
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        departamentCreate = service_manager.departament_service.create_departament(data, 'root')#get_jwt_identity())
        if departamentCreate is None:
            return jsonify({'error': 'Internal Server'}), 500   
        
        return jsonify({'message': 'Departament created'}), 201
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500    