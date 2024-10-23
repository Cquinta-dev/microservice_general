from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.departament_schema import expected_fields_create
from ..schemas.departament_schema import expected_fields_update
from ..utils.constants import constants

departament_routes = Blueprint('departament', __name__)

#Method for create departament.
@departament_routes.route('/createDepartament',methods=['POST'])
@jwt_required()
def create_departament():
   
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
    
    missing_fields = expected_fields_create - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400
    
    createDepartament = service_manager.departament_service.create_departament(data, get_jwt_identity())
    if createDepartament is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500   
    
    return jsonify({'message': 'Departament created'}), 201
    

#Method for get list to depataments.
@departament_routes.route('/allDepartaments', methods=['GET'])
@jwt_required()
def get_all_departaments():

    allDepartaments = service_manager.departament_service.get_all_departaments()
    if allDepartaments is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(allDepartaments), 200    


#Method for get one departament.
@departament_routes.route('/getDepartament', methods=['GET'])
@jwt_required()
def get_departament():

    id = request.args.get('id')
    if id is None: 
        return jsonify({'error': constants.NOT_ID}), 400    
    
    getDepartament = service_manager.departament_service.get_departament(id)
    if getDepartament is None:
        return jsonify({'error':'Departament not found'}), 404

    return jsonify(getDepartament), 200


#Method for udpate departament.
@departament_routes.route('/updateDepartament', methods=['PUT'])
@jwt_required()
def update_departament():    
              
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
        
    missing_fields = expected_fields_update - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400

    updateDepartament = service_manager.departament_service.update_departament(data, get_jwt_identity())
    if updateDepartament is constants.NOT_FOUND:
        return jsonify({'error':'Departament not found'}), 404
    
    if updateDepartament is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500
            
    return jsonify({'message': 'Departament updated'}), 201
