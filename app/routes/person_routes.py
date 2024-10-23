from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.person_schema import expected_fields_create
from ..schemas.person_schema import expected_fields_update
from ..utils.constants import constants

person_routes = Blueprint('person', __name__)

#Method for create person.
@person_routes.route('/createPerson',methods=['POST'])
@jwt_required()
def create_person():
    
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
    
    missing_fields = expected_fields_create - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400
    
    personCreate = service_manager.person_service.create_person(data, get_jwt_identity())
    if personCreate is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500   
    
    return jsonify({'message': 'Person created'}), 201


#Method for get list to person.
@person_routes.route('/allPersons', methods=['GET'])
@jwt_required()
def get_all_persons():

    allPersons = service_manager.person_service.get_all_persons()
    if allPersons is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(allPersons), 200


#Method for get one person.
@person_routes.route('/getPerson', methods=['GET'])
@jwt_required()
def get_person():

    id = request.args.get('id')
    if id is None: 
        return jsonify({'error': constants.NOT_ID}), 400
    
    getPerson = service_manager.person_service.get_person(id)    
    if getPerson is None:
        return jsonify({'error':'Person not found'}), 404
    
    return jsonify(getPerson), 200


#Method for udpate person.
@person_routes.route('/updatePerson', methods=['PUT'])
@jwt_required()
def update_person():    
        
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
        
    missing_fields = expected_fields_update - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400

    updatePerson = service_manager.person_service.update_person(data, get_jwt_identity())
    if updatePerson is constants.NOT_FOUND:
        return jsonify({'error':'Person not found'}), 404
    
    if updatePerson is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500        
        
    return jsonify({'message': 'Person updated'}), 201