from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from ..schemas.currency_schema import expected_fields_create
from ..schemas.currency_schema import expected_fields_update
from ..services import service_manager
from ..utils.constants import constants

currency_routes = Blueprint('currency', __name__)

#Method for create person.
@currency_routes.route('/createCurrency',methods=['POST'])
#@jwt_required()
def create_currency():
          
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
    
    missing_fields = expected_fields_create - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400
    
    createCurrency = service_manager.currency_service.create_currency(data, 'root')#get_jwt_identity())
    if createCurrency is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500   
    
    return jsonify({'message': createCurrency}), 201


#Method for get list to currencies.
@currency_routes.route('/allCurrencies', methods=['GET'])
#@jwt_required()
def get_currencies():

    allCurrency = service_manager.currency_service.get_currencies()
    if allCurrency is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(allCurrency), 200    


#Method for get one corrency.
@currency_routes.route('/getCurrency', methods=['GET'])
#@jwt_required()
def get_combo_currencies():

    id = request.args.get('id')
    if id is None: 
        return jsonify({'error': constants.NOT_ID}), 400
    
    getCurrency = service_manager.currency_service.get_combo_currencies(id)
    if getCurrency is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404
    
    return jsonify(getCurrency), 200
    

#Method for udpate currency.
@currency_routes.route('/updateCurrency', methods=['PUT'])
#@jwt_required()
def update_currency():    

    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
        
    missing_fields = expected_fields_update - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400

    updateCurrency = service_manager.currency_service.update_currency(data, 'root')#get_jwt_identity())
    if updateCurrency is constants.NOT_FOUND:
        return jsonify({'error': updateCurrency + data['moneda']}), 404
    
    if updateCurrency is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500
        
    return jsonify({'message': updateCurrency}), 201