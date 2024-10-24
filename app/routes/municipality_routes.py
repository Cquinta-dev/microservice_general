from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from ..schemas.municipality_schema import expected_fields_create
from ..schemas.municipality_schema import expected_fields_update
from ..services import service_manager
from ..utils.constants import constants

municipality_routes = Blueprint('municipality', __name__)

#Method for create municipality.
@municipality_routes.route('/createMunicipality',methods=['POST'])
@jwt_required()
def create_municipality():

    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
    
    missing_fields = expected_fields_create - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400
    
    createMunicipality = service_manager.municipality_service.create_municipality(data, get_jwt_identity())
    if createMunicipality is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500   
    
    return jsonify({'message': createMunicipality}), 201
    

#Method for get list to municipalities.
@municipality_routes.route('/allMunicipalities', methods=['GET'])
@jwt_required()
def get_municipalities():

    allMunicipalities = service_manager.municipality_service.get_municipalities()
    if allMunicipalities is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(allMunicipalities), 200    


#Method for get combo municipality.
@municipality_routes.route('/getComboMunicipalities', methods=['GET'])
@jwt_required()
def get_combo_municipalities():

    id = request.args.get('id')
    if id is None: 
        return jsonify({'error': constants.NOT_ID}), 400    
    
    getMunicipality = service_manager.municipality_service.get_combo_municipalities(id)
    if getMunicipality is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404
    
    return jsonify(getMunicipality), 200


#Method for udpate municipality.
@municipality_routes.route('/updateMunicipality', methods=['PUT'])
@jwt_required()
def update_municipality():    
      
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
        
    missing_fields = expected_fields_update - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400

    updateMunicipality = service_manager.municipality_service.update_municipality(data, get_jwt_identity())
    if updateMunicipality is constants.NOT_FOUND:
        return jsonify({'error': updateMunicipality + data['muncipalidad']}), 404
    
    if updateMunicipality is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500    
        
    return jsonify({'message': updateMunicipality}), 201