from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from ..schemas.country_schema import expected_fields_create
from ..schemas.country_schema import expected_fields_update
from ..services import service_manager
from ..utils.constants import constants

country_routes = Blueprint('country', __name__)

#Method for create country.
@country_routes.route('/createCountry',methods=['POST'])
@jwt_required()
def create_country():

    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
    
    missing_fields = expected_fields_create - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400
    
    createCountry = service_manager.country_service.create_country(data, get_jwt_identity())
    if createCountry is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500   
    
    return jsonify({'message': createCountry}), 201


#Method for get list to coutries.
@country_routes.route('/allCoutries', methods=['GET'])
@jwt_required()
def get_countries():

    allCoutries = service_manager.country_service.get_countries()
    if allCoutries is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(allCoutries), 200    


#Method for get enabled country for combo.
@country_routes.route('/getComboCountries', methods=['GET'])
@jwt_required()
def get_combo_countries():

    getComboCountry = service_manager.country_service.get_combo_countries()
    if getComboCountry is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404
        
    return jsonify(getComboCountry), 200


#Method for udpate country.
@country_routes.route('/updateCountry', methods=['PUT'])
@jwt_required()
def update_country():    
    
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
        
    missing_fields = expected_fields_update - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400

    updateCountry = service_manager.country_service.update_country(data, get_jwt_identity())
    if updateCountry is constants.NOT_FOUND:
        return jsonify({'error': updateCountry + data['pais']}), 404
    
    if updateCountry is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500
    
    return jsonify({'message': updateCountry}), 201