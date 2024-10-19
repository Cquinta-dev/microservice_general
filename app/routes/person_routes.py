from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.person_schema import expected_fields_create
from ..schemas.person_schema import expected_fields_update

person_routes = Blueprint('person', __name__)

#Method for create person.
@person_routes.route('/createPerson',methods=['POST'])
@jwt_required()
def create_person():

    try:        
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        personCreate = service_manager.person_service.create_person(data, get_jwt_identity())
        if personCreate is None:
            return jsonify({'error': 'Internal Server'}), 500   
        
        return jsonify({'message': 'Person created'}), 201
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500    


#Method for get list to person.
@person_routes.route('/allPersons', methods=['GET'])
@jwt_required()
def get_persons():

    personsGetAll = service_manager.person_service.get_all_persons()
    if personsGetAll is None:
        return jsonify({'error':'Not list data found'}), 404

    return jsonify(personsGetAll), 200


#Method for get one person.
@person_routes.route('/getPerson', methods=['GET'])
@jwt_required()
def get_person():

    personID = request.args.get('id')
    if personID: 
        personGet = service_manager.person_service.get_person(personID)
        if personGet is None:
            return jsonify({'error':'Person not found'}), 404
        
        return jsonify(personGet), 200

    return jsonify({'error': 'Id was not provided'}), 400


#Method for udpate person.
@person_routes.route('/updatePerson', methods=['PUT'])
@jwt_required()
def update_person():    

    try:        
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        missing_fields = expected_fields_update - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400

        personUpdate = service_manager.person_service.update_person(data, get_jwt_identity())
        if personUpdate is None:
            return jsonify({'error':'Person not found'}), 404
            
        return jsonify({'message': 'Person updated'}), 201

    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500    
